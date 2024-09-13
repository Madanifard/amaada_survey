from rest_framework import serializers
from survey.models.questions import Questions
from survey.models.options import Options


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['key', 'value']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Questions
        fields = ['id', 'survey', 'text', 'type', 'options']

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        question = Questions.objects.create(**validated_data)
        for option_data in options_data:
            Options.objects.create(question=question, **option_data)

        new_question = Questions.objects.prefetch_related('options').get(
            pk=question.id)
        return new_question

    def update(self, instance, validated_data):
        options_data = validated_data.pop('options')
        instance.text = validated_data.get('text', instance.text)
        instance.type = validated_data.get('type', instance.type)
        instance.save()

       # Update options
        if options_data:
            existing_option_ids = [
                option.id for option in instance.options.all()]
            new_option_ids = [
                option_data.get('id') for option_data in options_data if option_data.get('id')]

            # Delete removed options
            for option_id in existing_option_ids:
                if option_id not in new_option_ids:
                    Options.objects.get(id=option_id).delete()

            # Update or create options
            for option_data in options_data:
                option_id = option_data.get('id')
                if option_id:
                    option_instance = Options.objects.get(id=option_id,
                                                          question=instance)
                    option_instance.key = option_data.get('key',
                                                          option_instance.key)
                    option_instance.value = option_data.get('value',
                                                            option_instance.value)
                    option_instance.save()
                else:
                    Options.objects.create(question=instance, **option_data)

        return instance
