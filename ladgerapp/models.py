from django.db import models

# Create your models here.
class Laddger(models.Model):
	account_name = models.CharField(max_length = 255)

	def __str__(self):
		return self.account_name

class Journal(models.Model):
    Particulars = models.CharField(max_length=50)
    Debit = models.DecimalField(max_digits=10,decimal_places=2)
    Credit = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()
    Accounthead = models.ForeignKey(Laddger,on_delete=models.CASCADE)
    #adding total amount
    # TotalBal= models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.Particulars
