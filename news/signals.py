from django.db.models.signals import post_save, m2m_changed
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Post, SubscribersCategory, PostCategory
from django.dispatch import receiver
from .tasks import notify_subscribers


@receiver(post_save, sender=SubscribersCategory)
def notify_user_subscribe(sender, instance, created, **kwargs):
    subject = f'Подписка оформлена!'
    send_mail(
        subject=subject,
        message=f'Вы успешно подписались на категорию {instance.category.name}',
        from_email='andrej.krasikov@mail.ru',
        recipient_list=[f'{instance.subscriber.email}'],
    )


@receiver(m2m_changed, sender=Post.category.through, dispatch_uid='notify_post_created_signal')
def notify_post_created(sender, instance, action, **kwargs):
    if action == 'post_add':
        notify_subscribers.apply_async([instance.id], countdown=10)
