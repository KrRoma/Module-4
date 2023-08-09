from django.db import models

class Advertisement(models.Model):
    title=models.CharField('заголовок', max_length=128)
    description=models.TextField('описание')
    prise=models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction=models.BooleanField('торг',help_text='Отметьте если торг уместен')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title} , price={self.prise})'

    class Meta:
        db_table='advertisements'