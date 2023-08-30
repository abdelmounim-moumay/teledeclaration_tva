from django.db import models

class Tiers(models.Model):
    nom= models.CharField(max_length=100)
    If= models.CharField(max_length=20)
    ICE= models.CharField(max_length=20)
    
    def __str__(self):
        return self.nom

class Facture(models.Model):
    tiers: models.ForeignKey(Tiers, on_delete=models.CASCADE)
    numero_ordre = models.PositiveBigIntegerField()
    numero_Facture = models.CharField(max_length=20)
    date_Facture = models.DateField()
    montant_Ht = models.DecimalField(max_digits=10, decimal_places=2)
    taux_tva = models.DecimalField(max_digits=4, decimal_places=2)
    montant_tva = models.DecimalField(max_digits=2, decimal_places=2)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    mode_payement = models.PositiveSmallIntegerField(choices=(
        (1, 'especes'),
        (2, 'cheque'),
        (3, 'virement'),
        (7, 'autres'),

    ))
    date_paiement = models.DateField()

    def __str__(self):
        return f"Facture {self.numero_Facture} de {self.tiers}"
    

class Declaration(moldels.Model):
    RAISON_SOCIAL = models.CharField(max_length=100)
    ID_FISCAL = models.CharField(max_length=20)
    ANNEE = models.PositiveIntegerField()
    PERIODE = models.CharField(max_length=10)
    Regime_choices = (
        ('A', 'Régime d’encaissement N° 1 pour la declaration mensuelle'),
        ('B', 'Régime d’encaissement N° 2 pour la declaration Trimestriel'),
    )
    REGIME = models.CharField(max_length=1, choices=REGIME_CHOICES)
    factures_fournisseur = models.ManyToManyField(Facture, related_name='declarations_fournisseur', blank=True)
    factures_clients = models.ManyToManyField(Facture, related_name='declarations_clients', blank=True)
    total_deductions = models.DecimalField(max_digits=10, decimal_places=2)
    report_credit_TVA = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Déclaration {self.RAISON_SOCIAL} - {self.ANNEE} ({self.PERIODE})"