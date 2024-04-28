from django.db import models

# Create your models here.
class Vendor(models.Model):
    name= models.CharField(max_length=250)
    contact_details=models.IntegerField(max_length=10)
    address=models.CharField(max_length=250)
    vendor_code=models.CharField(unique=True)
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        ordering=['name']


class Purchase_Order(models.Model):
    PENDING='Pending'
    COMPLETED='Completed'
    CANCELLED='Cancelled'
    STATUS_CHOICES=[
        (PENDING,'Pending'),
        (COMPLETED,'Completed'),
        (CANCELLED,'Cancelled')
    ]
    po_number=models.CharField(unique=True)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default=PENDING)
    quality_rating=models.FloatField(null=True)
    issue_date=models.DateTimeField()
    acknowledgement_date=models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.po_number}"
    
    class Meta:
        ordering=['po_number']

class Historial_performance:
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date=models.DateTimeField
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()

    



