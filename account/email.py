'''
get_email_sent(request,receiver=[],subject='',context = {},template='emails/progress.html') 

'''
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def function(request,**kwargs):
   sender = settings.EMAIL_HOST_USER
   receiver = kwargs['receiver']
   subject = kwargs['subject']
   context = kwargs['context']
   html_content = render_to_string(kwargs['template'], context) # render with dynamic value
   text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
   email = EmailMultiAlternatives(subject, text_content, sender, receiver)
   email.attach_alternative(html_content, "text/html")
   email.send(fail_silently=True)
   return True
