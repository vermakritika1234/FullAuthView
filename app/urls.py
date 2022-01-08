from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm , MypasswordchangeForm,MyPasswordResetForm,MySetPasswordForm
import uuid

urlpatterns = [
    # path('', views.home, name="index"),
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/login.html",authentication_form=LoginForm), name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('admin_upload/',views.admin_upload,name="admin_upload"),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class= MypasswordchangeForm, 
    success_url='/passwordchangedone/'), name='passwordchange'),

    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html' ),name='passwordchangedone'),
  #--1 for password reset 
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name="password_reset"),
   
   #2-for password reset doen
   path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name="password_reset_done"),
   
  #  #3--PASSWORD RESET DONE CONFIRM
   path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',
   form_class=MySetPasswordForm),name='password_reset_confirm'),
 
  #   #4 passwrod reset finally complete now u can login paart
     path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
  
    # path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class= MypasswordchangeForm, 
    # success_url='/passwordchangedone/'), name='passwordchange'),
    # path('passwordchagneDone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone'),name='password_change_done'),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)