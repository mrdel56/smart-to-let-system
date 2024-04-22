from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            # Send email
            send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\nMessage: {message}",
                email,
                ["your_email@example.com"],  # Replace with your email
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact_success")
    else:
        form = ContactForm()

    return render(request, "contact_form.html", {"form": form})


def contact_success(request):
    return render(request, "contact_success.html")
