from django.contrib import messages

# from properties.models import PropertyOwner
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from userapp.models import UserInfo

from .models import CreditPackage, Transaction

# Credit Package Views


def credit_package_list(request):
    packages = CreditPackage.objects.all()
    return render(request, "credit_package_list.html", {"packages": packages})


def add_credit_package(request):
    if request.method == "POST":
        package_name = request.POST.get("package_name")
        price = request.POST.get("price")
        credit = request.POST.get("credit")

        CreditPackage.objects.create(
            package_name=package_name, price=price, credit=credit
        )
        messages.success(request, "Credit package added successfully!")
        return redirect("credit_package_list")

    return render(request, "add_credit_package.html")


def edit_credit_package(request, package_id):
    package = CreditPackage.objects.get(id=package_id)

    if request.method == "POST":
        package.package_name = request.POST.get("package_name")
        package.price = request.POST.get("price")
        package.credit = request.POST.get("credit")
        package.save()

        messages.success(request, "Credit package updated successfully!")
        return redirect("credit_package_list")

    return render(request, "edit_credit_package.html", {"package": package})


def delete_credit_package(request, package_id):
    package = CreditPackage.objects.get(id=package_id)
    package.delete()
    messages.success(request, "Credit package deleted successfully!")
    return redirect("credit_package_list")


# Transaction Views


def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, "transaction_list.html", {"transactions": transactions})


# def add_transaction(request):
#     if request.method == "POST":
#         owner_id = request.POST.get("owner_id")
#         package_id = request.POST.get("package_id")
#         transaction_id = request.POST.get("transaction_id")
#         amount = request.POST.get("amount")
#         transaction_method = request.POST.get("transaction_method")

#         owner = user.objects.get(id=owner_id)
#         package = CreditPackage.objects.get(id=package_id)

#         Transaction.objects.create(
#             owner=owner,
#             package=package,
#             transaction_id=transaction_id,
#             amount=amount,
#             transaction_method=transaction_method,
#         )
#         messages.success(request, "Transaction added successfully!")
#         return redirect("transaction_list")

#     return render(request, "add_transaction.html")


def delete_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    transaction.delete()
    messages.success(request, "Transaction deleted successfully!")
    return redirect("transaction_list")


def add_transaction(request):
    if request.method == "POST":

        # print("data = ", request.POST)

        user_id = request.POST.get("user_id")
        package_id = request.POST.get("package_id")
        transaction_id = request.POST.get("transaction_id")
        # amount = float(request.POST.get("amount"))
        # transaction_method = request.POST.get("transaction_method")

        try:
            owner = User.objects.get(id=user_id)
            userProfile = UserInfo.objects.filter(user=user_id).first()
            package = CreditPackage.objects.get(id=package_id)

            Transaction.objects.create(
                owner=owner,
                package=package,
                transaction_id=transaction_id,
                amount=package.price,
                transaction_method="BKASH",
            )

            if not userProfile:

                print("not user profile fired")

                userProfile = UserInfo.objects.create(
                    user=owner,
                    first_name=owner.first_name,
                    last_name=owner.last_name,
                    phone="",
                    address="",
                    image="",
                    credit=package.credit,
                )
            else:
                userProfile.credit += package.credit
                userProfile.save()

            messages.success(
                request, "Buy credit successfully and user credit updated!"
            )
            return redirect("credits")

        except User.DoesNotExist:
            messages.error(request, "User does not exist!")
        except CreditPackage.DoesNotExist:
            messages.error(request, "Credit package does not exist!")

    properties = request.user.property_set.all()
    propertyCount = len(properties)

    return render(request, "add_transaction.html", {"propertyCount": propertyCount})
