from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from celery import shared_task
from .models import Category, Post
from datetime import datetime, timedelta


@shared_task
def mailing_subscribers():
    context = {}
    for category in Category.objects.all():
        context['category'] = category
        context['posts'] = category.post_set.filter(time_create__gte=datetime.utcnow() - timedelta(days=7))
        for subscriber in category.subscribers.all():
            message = get_template('mail_mailing.html').render(context | {'user': subscriber})
            msg = EmailMessage('Еженедельная рассылка новостей MainNews!',
                               message,
                               'andrej.krasikov@mail.ru',
                               [subscriber.email])
            msg.content_subtype = 'html'
            msg.send()


@shared_task
def notify_subscribers(post_id):
    post = Post.objects.get(pk=post_id)
    recipient_list = []
    for category in post.category.all():
        for subscriber in category.subscribers.all():
            recipient_list.append(subscriber.email)
    html_content = render_to_string('news/mail_subscribers.html', {'post': post})
    msg = EmailMultiAlternatives(
        subject=f'{post.title_post}',
        from_email='andrej.krasikov@mail.ru',
        to=recipient_list
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()