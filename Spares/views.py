from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Maker, PumpModel, ModelVariant, ModelPart, ModelVariantPart 
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.templatetags.static import static


def get_pumpmodels(request, id):
    pumpmodels = PumpModel.objects.filter(maker_id=id)
    data = list(pumpmodels.values('id', 'name'))
    return JsonResponse(data, safe=False)

def get_model_varient(request, id):
    variants = ModelVariant.objects.filter(model_id=id)
    data = list(variants.values('id', 'discharge_diameter', 'stages'))
    return JsonResponse(data, safe=False)

def get_parts(request, model_id, variant_id):
    # Fetch common parts (for model)
    common_parts = ModelPart.objects.filter(model_id=model_id).select_related('part')
    common_parts_data = [
        {
            'id': mp.part.id,
            'part_no': mp.part.part_no,
            'name': mp.part.name,
            'material': mp.part.material,
            'technical_details':mp.part. technical_details,
            'drawing_file': mp.part.drawing_file.url if mp.part.drawing_file else '',
            'cad_file': mp.part.cad_file.url if mp.part.cad_file else '',
            'mapping': mp.part.mapping.url if mp.part.mapping else '',
        }
        for mp in common_parts
    ]

    # Fetch variant parts (specific to variant)
    variant_parts = ModelVariantPart.objects.filter(variant_id=variant_id).select_related('part')
    variant_parts_data = [
        {
            'id': vp.part.id,
            'part_no': vp.part.part_no,
            'name': vp.part.name,
            'material': vp.part.material,
            'technical_details':vp.part. technical_details,
            'drawing_file': vp.part.drawing_file.url if vp.part.drawing_file else '',
            'cad_file': vp.part.cad_file.url if vp.part.cad_file else '',
            'mapping': vp.part.mapping.url if vp.part.mapping else '',
        }
        for vp in variant_parts
    ]

    return JsonResponse({
        'common_parts': common_parts_data,
        'variant_parts': variant_parts_data,
    })
@login_required
def maker_model(request):
    makers = Maker.objects.all()
    return render(request, 'Spares/MakerModel.html', {'makers': makers})
@login_required
def spareparts(request):
    return render(request, 'Spares/Chatbotpart.html')
