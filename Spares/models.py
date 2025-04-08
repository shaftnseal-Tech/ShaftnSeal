from django.db import models

# Maker Table
class Maker(models.Model):
    name = models.CharField(max_length=100, verbose_name="Maker Name")

    def __str__(self):
        return self.name


# Pump Model Table
class PumpModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, related_name='pump_models')
    name = models.CharField(max_length=100, verbose_name="Model Name")
    
    def __str__(self):
        return f"{self.maker.name} - {self.name}"


# Variant Table
class ModelVariant(models.Model):
    model = models.ForeignKey(PumpModel, on_delete=models.CASCADE, related_name='variants')
    discharge_diameter = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Discharge Diameter (mm)")
    stages = models.IntegerField(verbose_name="Number of Stages")

    def __str__(self):
        return f"{self.model.name} - {self.discharge_diameter}mm - {self.stages} stages"


# Parts Table
class Part(models.Model):
    part_no = models.CharField(max_length=50, verbose_name="Part Number")
    name = models.CharField(max_length=100, verbose_name="Part Name")
    material = models.CharField(max_length=100, blank=True, null=True, verbose_name="Material")
    technical_details = models.TextField(blank=True, null=True, verbose_name="Technical Details")
    drawing_file = models.FileField(upload_to='drawings/', blank=True, null=True, verbose_name="Drawing File")
    cad_file = models.FileField(upload_to='cad_files/', blank=True, null=True, verbose_name="CAD File")
    mapping = models.FileField(upload_to='mapping_files/',blank=True,null=True,verbose_name="Mapping File")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.part_no} - {self.name}"


# Mapping parts to Variants
class ModelVariantPart(models.Model):
    variant = models.ForeignKey(ModelVariant, on_delete=models.CASCADE, related_name='variant_parts')
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['variant', 'part'], name='unique_variant_part')
        ]

    def __str__(self):
        return f"Variant {self.variant} -> Part {self.part.part_no} - {self.part.name}"
    
class ModelPart(models.Model):
    model = models.ForeignKey(PumpModel, on_delete=models.CASCADE, related_name='common_parts')
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    
    
    

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['model', 'part'], name='unique_model_part')
        ]
    def __str__(self):
        return f"Common Part for {self.model}: {self.part}"


   