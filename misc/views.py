from django.shortcuts import render
import os


def faq(request):
    page_title = "FAQ"
    return render(request, "misc/faq.html", { "page_title": page_title })


def our_story(request):
    page_title = "Our Story"
    return render(request, "misc/our_story.html", { "page_title": page_title })


def store(request):
    page_title = "Store"
    return render(request, "misc/store.html", { "page_title": page_title })


def contact_us(request):
    if request.method == "POST":
        data = request.POST
        os.system('echo %s > /home/michel/pharma_aid/misc/mail/mail.txt' % data['message'])
        os.system('mail -s "Email from a Customer" hasan.mohaiminul@gmail.com < /home/michel/pharma_aid/misc/mail/mail.txt')
    page_title = "Contact Us"
    if request.user.is_authenticated():
        name = request.user.get_full_name()
        phone = request.user.mobile
        email = request.user.email
    else:
        name = ''
        phone = ''
        email = ''
    return render(request, "misc/contact_us.html", { "page_title": page_title,
                                                     "name": name,
                                                     "phone": phone,
                                                     "email": email
                                                     })


def terms_of_use(request):
    page_title = "Terms of Use"
    return render(request, "misc/terms_of_use.html", { "page_title": page_title })
