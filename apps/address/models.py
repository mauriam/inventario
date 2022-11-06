from django.db import models

# nacionalidad


class TpsNationalityModel(models.Model):
    nationality_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10,unique=True, verbose_name='Nacionalidad')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TpsNationality'
# estado


class TpsStateModel(models.Model):
    state_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10,unique=True, verbose_name='Estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TpsState'
# municipio


class TpsMunicipalityModel(models.Model):
    municipality_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, verbose_name='Municipio')
    is_capital = models.BooleanField(default=False,verbose_name='Es Capital')
    fk_state_id = models.ForeignKey(TpsStateModel, on_delete=models.CASCADE,verbose_name='Estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TpsMunicipality'
# ciudad


class TpsCityModel(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, verbose_name='Ciudad')
    is_capital = models.BooleanField(default=False,verbose_name='Es Capital')
    fk_municipality_id = models.ForeignKey(TpsMunicipalityModel, on_delete=models.CASCADE,verbose_name='Municipio')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TpsCity'
# Parroquia


class TpsParishCouncilModel(models.Model):
    parish_council_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, verbose_name='Parroquia')
    fk_state_id = models.ForeignKey(TpsCityModel, on_delete=models.CASCADE,verbose_name='Ciudad')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TpsParishCouncil'
# direccion


class AddressModel(models.Model):
    address_id = models.AutoField(primary_key=True)
    fk_state = models.ForeignKey(TpsStateModel, on_delete=models.DO_NOTHING,verbose_name='Estado')
    fk_municipality = models.ForeignKey(TpsMunicipalityModel, on_delete=models.DO_NOTHING,verbose_name='Municipio')
    fk_city = models.ForeignKey(TpsCityModel, on_delete=models.DO_NOTHING,verbose_name='Ciudad')
    fk_parish_council = models.ForeignKey(
        TpsParishCouncilModel, on_delete=models.DO_NOTHING,verbose_name='Parroquia')
    sector = models.CharField(max_length=50, verbose_name='Sector')
    street = models.CharField(max_length=50, verbose_name='Calle')
    house = models.CharField(max_length=50, verbose_name='Casa')

    def __str__(self):
        return (
            self.house, ' ',
            self.street, ' ',
            self.sector, ' ',
            self.fk_parish_council.__str__, ' ',
            self.fk_city.__str__, ' ',
            self.fk_municipality.__str__, ' ',
            self.fk_state.__str__
        )
