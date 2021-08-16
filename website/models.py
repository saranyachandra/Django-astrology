from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.
class Website(models.Model):
    
    name = models.CharField(max_length=60)
    img  = models.ImageField(upload_to='profile_img', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (300,300), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'profile_img-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.profile_img.save(fname,File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)   