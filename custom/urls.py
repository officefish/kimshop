__author__ = 'inozemcev'
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from oscar.apps.checkout.views import ShippingAddressView
from oscar.apps.promotions.views import HomeView

from oscar.apps.customer.views import AccountAuthView
from oscar.apps.customer.views import LogoutView
from oscar.apps.customer.views import AccountRegistrationView
from oscar.apps.customer.views import ChangePasswordView

from oscar.apps.customer.views import ProfileView, ProfileUpdateView

from oscar.apps.customer.views import OrderHistoryView, OrderDetailView

from oscar.apps.customer.views import EmailHistoryView, EmailDetailView

from oscar.apps.customer.views import AddressListView, AddressCreateView, AddressUpdateView

from oscar.apps.customer.alerts.views import ProductAlertListView

from oscar.apps.customer.wishlists.views import WishListListView, WishListCreateView, WishListDetailView

from oscar.apps.customer.notifications.views import InboxView, ArchiveView

from oscar.apps.catalogue.views import ProductDetailView, ProductCategoryView

from oscar.apps.catalogue.reviews.views import CreateProductReview

from custom.views import  get_media_url, temp


urlpatterns = [
    url(r'^ru/checkout/shipping-address/', ShippingAddressView.as_view(template_name="custom/checkout/shipping_address.html"), name="custom_shipping_address"),
]


# promotions urls
urlpatterns += [
    url(r'^ru/$', HomeView.as_view(template_name="custom/promotions/home.html"), name='ru_home'),
]

# customer urls
# 1 / Login, logout and register doesn't require login
urlpatterns += [
            url(r'login/$', AccountAuthView.as_view(template_name="custom/customer/login.html"), name='login'),
            url(r'logout/$', LogoutView.as_view(), name='logout'),
            url(r'register/$', AccountRegistrationView.as_view(template_name="custom/customer/register.html"), name='register'),
            url(r'change-password/$',
                login_required(ChangePasswordView.as_view(template_name="custom/customer/profile/change_password_form.html")),
                name='change-password'),

]

# 2 / Profile
urlpatterns += [
            url(r'profile/$', ProfileView.as_view(template_name="custom/customer/profile/profile.html"), name='profile-view'),
            url(r'profile/edit/$',
                login_required(ProfileUpdateView.as_view(template_name="custom/customer/profile/profile_form.html")),
                name='profile-update'),
]


# 3 / Orders
urlpatterns += [
     url(r'^ru/accounts/orders/$',
                login_required(OrderHistoryView.as_view(template_name='custom/customer/order/order_list.html')),
                name='order-list'),
     url(r'^ru/accounts/orders/(?P<order_number>\d+)/$',
                login_required(OrderDetailView.as_view(template_name='custom/customer/order/order_detail.html')),
                name='order'),
]



# 4 / Emails
urlpatterns += [
    url(r'^ru/accounts/emails/$',
                login_required(EmailHistoryView.as_view(template_name='custom/customer/email/email_list.html')),
                name='email-list'),

    url(r'^ru/accounts/emails/(?P<email_id>\d+)/$',
                login_required(EmailDetailView.as_view(template_name='custom/customer/email/email_detail.html')),
                name='email-detail'),

]


# 5 / Addresses
urlpatterns += [
     url(r'^ru/accounts/addresses/$',
                login_required(AddressListView.as_view(template_name='custom/customer/address/address_list.html')),
                name='address-list'),
     url(r'^ru/accounts/addresses/add/$',
                login_required(AddressCreateView.as_view(template_name='custom/customer/address/address_create.html')),
                name='address-create'),
     url(r'^ru/accounts/addresses/(?P<pk>\d+)/$',
                login_required(AddressUpdateView.as_view(template_name='custom/customer/address/address_create.html')),
                name='address-detail'),
]


# 6 / Alerts
urlpatterns += [
     url(r'^ru/accounts/alerts/$',
                login_required(ProductAlertListView.as_view(template_name='custom/customer/alerts/alert_list.html')),
                name='alerts-list'),
]

# 7 / Wishlists
urlpatterns += [
     url(r'^ru/accounts/wishlists/$',
                login_required(WishListListView.as_view(template_name='custom/customer/wishlists/wishlists_list.html')),
                name='wishlists-list'),
     url(r'^ru/accounts/wishlists/create/$',
                login_required(WishListCreateView.as_view(template_name='custom/customer/wishlists/wishlists_form.html')),
                name='wishlists-create'),
      url(r'ru/accounts/wishlists/create/with-product/(?P<product_pk>\d+)/$',
                login_required(WishListCreateView.as_view(template_name='custom/customer/wishlists/wishlists_form.html')),
                name='wishlists-create-with-product'),
     url(r'^ru/accounts/wishlists/(?P<key>[a-z0-9]+)/$',
                WishListDetailView.as_view(template_name='custom/customer/wishlists/wishlists_detail.html'), name='wishlists-detail'),

]




urlpatterns += [
     url(r'^ru/accounts/notifications/inbox/$',
                login_required(InboxView.as_view(template_name='custom/customer/notifications/list.html')),
                name='notifications-inbox'),
     url(r'^ru/accounts/notifications/archive/$',
                login_required(ArchiveView.as_view(template_name='custom/customer/notifications/list.html')),
                name='notifications-archive'),
]


# catalogue
urlpatterns += [
     url(r'^ru/catalogue/$', ProductCategoryView.as_view(template_name='custom/catalogue/browse.html'), name='index'),
     url(r'^ru/catalogue/(?P<product_slug>)[\w-]*_(?P<pk>\d+)/$',
                ProductDetailView.as_view(template_folder = "custom/catalogue"), name='detail'),
     url(r'^ru/catalogue/category/(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/images/products/(?P<year>\d+)/(?P<mouth>\d+)/(?P<img>.*)/$', temp),
     url(r'^ru/catalogue/category/(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/$',
                ProductCategoryView.as_view(template_name='custom/catalogue/browse.html'), name='category'),
     url(r'^ru/catalogue/category/(?P<category_slug>[\w-]+(/[\w-]+)*)/$',
                 ProductCategoryView.as_view(template_name='custom/catalogue/browse.html')),

]

# reviews
urlpatterns += [
     url(r'^ru/catalogue/(?P<product_slug>[\w-]*)_(?P<product_pk>\d+)/reviews/add/$',
         CreateProductReview.as_view(template_name='custom/catalogue/reviews/review_form.html'), name='reviews-add'),


]

# English version

# promotions urls
urlpatterns += [
    url(r'^en/$', HomeView.as_view(template_name="custom/promotions/home.html"), name='home'),
]


# 3 / Orders
urlpatterns += [
     url(r'^en/accounts/orders/$',
                login_required(OrderHistoryView.as_view(template_name='custom/customer/order/order_list.html')),
                name='order-list'),
     url(r'^en/accounts/orders/(?P<order_number>\d+)/$',
                login_required(OrderDetailView.as_view(template_name='custom/customer/order/order_detail.html')),
                name='order'),
]



# 4 / Emails
urlpatterns += [
    url(r'^en/accounts/emails/$',
                login_required(EmailHistoryView.as_view(template_name='custom/customer/email/email_list.html')),
                name='email-list'),

    url(r'^en/accounts/emails/(?P<email_id>\d+)/$',
                login_required(EmailDetailView.as_view(template_name='custom/customer/email/email_detail.html')),
                name='email-detail'),

]


# 5 / Addresses
urlpatterns += [
     url(r'^en/accounts/addresses/$',
                login_required(AddressListView.as_view(template_name='custom/customer/address/address_list.html')),
                name='address-list'),
     url(r'^en/accounts/addresses/add/$',
                login_required(AddressCreateView.as_view(template_name='custom/customer/address/address_create.html')),
                name='address-create'),
     url(r'^en/accounts/addresses/(?P<pk>\d+)/$',
                login_required(AddressUpdateView.as_view(template_name='custom/customer/address/address_create.html')),
                name='address-detail'),
]


# 6 / Alerts
urlpatterns += [
     url(r'^en/accounts/alerts/$',
                login_required(ProductAlertListView.as_view(template_name='custom/customer/alerts/alert_list.html')),
                name='alerts-list'),
]

# 7 / Wishlists
urlpatterns += [
     url(r'^en/accounts/wishlists/$',
                login_required(WishListListView.as_view(template_name='custom/customer/wishlists/wishlists_list.html')),
                name='wishlists-list'),
     url(r'^en/accounts/wishlists/create/$',
                login_required(WishListCreateView.as_view(template_name='custom/customer/wishlists/wishlists_form.html')),
                name='wishlists-create'),
      url(r'en/accounts/wishlists/create/with-product/(?P<product_pk>\d+)/$',
                login_required(WishListCreateView.as_view(template_name='custom/customer/wishlists/wishlists_form.html')),
                name='wishlists-create-with-product'),
     url(r'^en/accounts/wishlists/(?P<key>[a-z0-9]+)/$',
                WishListDetailView.as_view(template_name='custom/customer/wishlists/wishlists_detail.html'), name='wishlists-detail'),

]




urlpatterns += [
     url(r'^en/accounts/notifications/inbox/$',
                login_required(InboxView.as_view(template_name='custom/customer/notifications/list.html')),
                name='notifications-inbox'),
     url(r'^en/accounts/notifications/archive/$',
                login_required(ArchiveView.as_view(template_name='custom/customer/notifications/list.html')),
                name='notifications-archive'),
]


# catalogue
urlpatterns += [
     url(r'^en/catalogue/$', ProductCategoryView.as_view(template_name='custom/catalogue/browse.html'), name='index'),
     url(r'^en/catalogue/(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$',
                ProductDetailView.as_view(template_folder = "custom/catalogue"), name='detail'),
     url(r'^en/catalogue/category/(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/$',
                ProductCategoryView.as_view(template_name='custom/catalogue/browse.html'), name='category'),
     url(r'^en/catalogue/category/(?P<category_slug>[\w-]+(/[\w-]+)*)/$',
                 ProductCategoryView.as_view(template_name='custom/catalogue/browse.html'))
]

# reviews
urlpatterns += [
     url(r'^en/catalogue/(?P<product_slug>[\w-]*)_(?P<product_pk>\d+)/reviews/add/$',
         CreateProductReview.as_view(template_name='custom/catalogue/reviews/review_form.html'), name='reviews-add'),


]
