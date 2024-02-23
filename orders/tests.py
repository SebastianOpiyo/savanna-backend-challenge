from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateAPIViewTestCase(APITestCase):
    url = reverse('order-list-create')  # Assuming 'order-list-create' is the URL name for OrderListCreateAPIView

    def test_create_order(self):
        data = {'name': 'Test Order', 'quantity': 5}  # Sample data for creating an order
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().name, 'Test Order')

    def test_list_orders(self):
        Order.objects.create(name='Order 1', quantity=3)
        Order.objects.create(name='Order 2', quantity=2)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Order 1')
        self.assertEqual(response.data[1]['name'], 'Order 2')

class OrderRetrieveUpdateDestroyAPIViewTestCase(APITestCase):
    def setUp(self):
        self.order = Order.objects.create(name='Test Order', quantity=5)
        self.url = reverse('order-detail', kwargs={'pk': self.order.pk})  # Assuming 'order-detail' is the URL name for OrderRetrieveUpdateDestroyAPIView

    def test_retrieve_order(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Order')

    def test_update_order(self):
        data = {'name': 'Updated Order', 'quantity': 10}
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.get(pk=self.order.pk).name, 'Updated Order')

    def test_delete_order(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)
