from django.conf.urls import url
from venue import views

app_name = "venue"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^door/(?P<event>\w+)/$', views.door, name='door'),
    url(r'^newcompany/', views.new_company, name='new_company'),
    url(r'^join/(?P<membershiptype>\w+)/$', views.new_member, name='new_member'),
    url(r'^joinguestlist/(?P<guestlist>\w+)/$', views.join_guestlist, name='join_guestlist'),
    url(r'^testpage', views.testpage, name='testpage'),
    url(r'^exportcsv/(?P<guestlist>\w+)/$', views.export_csv, name='exportcsv'),
    url(r'^ajax/toggleguestlistopen/$', views.toggle_guestlist_open, name='toggle_guestlist_open'),
    url(r'^ajax/doorarrival/$', views.door_ajax_arrival, name='door_ajax_arrival'),
    url(r'^ajax/deletelayout/$', views.delete_layout, name='delete_layout'),
    url(r'^ajax/eventdelete/$', views.ajax_event_delete, name='ajax_event_delete'),
    url(r'^ajax/recceventdeleteall/$', views.ajax_recc_event_delete_all, name='ajax_recc_event_delete_all'),
    url(r'^ajax/recceventdeletedate/$', views.ajax_recc_event_delete_date, name='ajax_recc_event_delete_ate'),
    url(r'^payment/(?P<membership>\w+)/$', views.payment, name='payment'),
    url(r'^(?P<company>\w+)/$', views.company, name='company'),
    url(r'^(?P<company>\w+)/newvenue/$', views.new_venue, name='new_venue'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/$', views.venue, name='venue'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/settings/$', views.venue_settings, name='venue_settings'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/guestlist/(?P<guestlist>\w+)/$', views.view_guestlist, name='view_guestlist'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/newguestlist/(?P<event>\w+)/$', views.new_guestlist, name='new_guestlist'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/event/new/$', views.new_event, name='new_event'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/event/newoneoff/$', views.new_one_off_event, name='new_one_off_event'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/event/newrecurring/$', views.new_recurring_event, name='new_recurring_event'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/event/recurring/(?P<event>\w+)/$', views.view_recurring_event, name='view_recurring_event'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/event/(?P<event>\w+)/$', views.view_event, name='view_event'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/members/$', views.members, name='members'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/members/newtype/$', views.new_membership_type, name='new_membership_type'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/members/import/$', views.import_members, name='import_members'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/layout/$', views.venue_layout, name='venue_layout'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/layout/create/$', views.new_venue_layout, name='new_venue_layout'),
    url(r'^(?P<company>\w+)/(?P<venue>\w+)/layout/createarea/(?P<layout>\w+)$', views.new_venue_layout_area, name='new_venue_layout_area'),
]
