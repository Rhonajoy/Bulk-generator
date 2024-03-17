from rest_framework import serializers
from .models import Product,ProductVariant

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductVariant
        fields=['id','sku','name','details','price', ]

class ProductSerializer(serializers.ModelSerializer):
    variants=ProductVariantSerializer(many=True,read_only=True)
    class Meta:
        model=Product
        fields=['id','name','image','variants']

        def create(self, validated_data):
            variants_data = validated_data.pop('variants', [])
            product = Product.objects.create(**validated_data)
            for variant_data in variants_data:
                ProductVariant.objects.create(product=product, **variant_data)
                print(variants_data)
            return product
            
            
            # variant_data = validated_data.pop('variants')
            # product = Product.objects.create(**validated_data)

            # for variants in variant_data:
            #     ProductVariant.objects.create(product=product, **variants)

            # return product
            
            
            # product = Product.objects.create(**validated_data)
            # ProductVariant.objects.create(product=product **variant_data)
            # return product
            

            # variants_data = validated_data.pop('variants', [])
            # product = Product.objects.create(**validated_data)
            # for variant_data in variants_data:
            #     ProductVariant.objects.create(product=product, **variant_data)
            # return product    