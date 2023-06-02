from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from accounts.models import MyOrders


# Create your views here.

def download_invoice(request, order_id):
    order = MyOrders.objects.filter(cart__razorpay_order_id=order_id).first()
    if order:
        cart_items = order.cart.cart_items.all()

        # Getting Cart total without Coupen

        cart_total_without_coupon = order.cart.get_cart_total_without_coupen(order_id)

        # Getting Minimum Amount of Coupon

        coupon = order.cart.coupen
        if coupon:
            minimum_amount = coupon.minimun_amount   
        else:
            minimum_amount = 0
        
        quantity = sum([cart_item.quantity if cart_item.quantity < cart_item.product.product_available_count else 0 for cart_item in cart_items])
        return render(request, "pdf_convert/bill.html", {'cart_items':cart_items, 'order':order, "quantity":quantity, 'minimum_amount':minimum_amount, 'cart_total_without_coupon': cart_total_without_coupon})
        # template_path = 'pdf_convert/bill.html'
        # context = {'cart_items':cart_items, 'order':order, "quantity":quantity, 'minimum_amount':minimum_amount, 'cart_total_without_coupon': cart_total_without_coupon}
        # # Create a Django response object, and specify content_type as pdf
        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = f'attachment; filename="Invoice-{order_id}.pdf"'
        # # find the template and render it.
        # template = get_template(template_path)
        # html = template.render(context)

        # # create a pdf
        # pisa_status = pisa.CreatePDF(html, dest=response)
        # # if error then show some funny view
        # if pisa_status.err:
        #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
        # return response