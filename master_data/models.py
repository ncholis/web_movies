from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Genre(models.Model):
    class Meta:
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')
    
    name = models.CharField(_('Name Genre'), max_length=100)
    _already_clean = False

    def __str__(self):
        return f'{self.name}'
    
    def clean_name(self):
        self.name = self.name and self.name.strip()

    def clean(self):
        self.clean_name()
        self._already_clean = True

    def save(self, *args, **kwargs):
        if not self._already_clean:
            self.clean()

        ret = super().save(*args, **kwargs)
        return ret

class MPAARating(models.Model):
    class Meta:
        verbose_name = _('MPAA Rating')
        verbose_name_plural = _('MPAA Rating')
    
    label = models.CharField(_('Label'), max_length=100)
    type = models.CharField(_('Type'), max_length=50)

    _already_clean = False

    def __str__(self):
        return f'{self.label} - {self.type}'

    def clean_label(self):
        self.label = self.label and self.label.strip()

    def clean(self):
        self.clean_label()
        self._already_clean = True

    def save(self, *args, **kwargs):
        if not self._already_clean:
            self.clean()

        ret = super().save(*args, **kwargs)
        return ret

class Movies(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')
    
    name = models.CharField(_('Title Movie'), max_length=255)
    description = models.TextField(_('Description'), blank=True, null=True)
    image = models.ImageField(_('Image'), upload_to='uploads/movies', blank=True, null=True)
    duration = models.PositiveBigIntegerField(_('Duration'), default=0)
    genre = models.ManyToManyField(Genre)
    language = models.CharField(_('Language'), max_length=50)
    mpaarating = models.ForeignKey('MPAARating', verbose_name=_('MPAA Rating'), null=True, on_delete=models.SET_NULL)
    user_rating = models.PositiveIntegerField(default=0, help_text="User Rating (1-5)")

    _already_clean = False


    def __str__(self):
        return f'{self.name}'
    
    def clean_user_rating(self):
        if not self.user_rating:
            return 0
        
        if self.user_rating > 5:
            raise ValidationError("Please Input Rating in range 1 - 5")

    def clean(self):
        self.clean_user_rating()
        self._already_clean = True

    def save(self, *args, **kwargs):
        if not self._already_clean:
            self.clean()

        ret = super().save(*args, **kwargs)
        return ret