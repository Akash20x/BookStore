from django.http import request
from django.urls import path
from . import views
from django.conf.urls.static import static
from bookstore.settings import MEDIA_URL,MEDIA_ROOT

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('see/<int:product_id>',views.see,name="see"),
    path('see2/<int:sold_id>',views.see2,name="see2"),
    path('orders',views.order,name="order"),
    path('checkout/<int:product_id>',views.checkout,name="checkout"),
    path('payment/<int:product_id>',views.payment,name="payment"),
    path('payment/verify',views.paymentverify,name="paymentverify"),
    path("sellbooks/", views.sellbooks, name="sellbooks"),
    path("old/", views.old, name="old"),

]+static(MEDIA_URL,document_root=MEDIA_ROOT)