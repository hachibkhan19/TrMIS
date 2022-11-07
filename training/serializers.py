from rest_framework import serializers
from course.models import Course
from batch.models import Batch

class BatchSerializer(serializers.ModelSerializer):
    trainees = serializers.IntegerField(source="trainee.count", read_only=True)

    class Meta:
        model = Batch
        fields = ["id", "batch_name", "trainees"]


class BatchByYear:
    def __init__(self, year, batches):
        self.year = year
        self.batches = batches


class BatchByYearSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    batches = serializers.SerializerMethodField()

    class Meta:
        model = BatchByYear
        fields = ['year', 'batches']


    def get_batches(self, batches):
        return BatchSerializer(batches.batches, many=True).data



class CourseSerializer(serializers.ModelSerializer):
        
    batchesByYear = serializers.SerializerMethodField()

    class Meta:
        
        model = Course
        fields = ("id", "name", "batchesByYear")
    
    def get_batchesByYear(self, name):
        years = Batch.objects.prefetch_related("trainee").filter(training_course_detail__course__name=name)
        years_dict = {}
        for year in years:
            if year.year in years_dict:
                new_year_list = years_dict.get(year.year) + [year]
                years_dict.update({year.year: new_year_list})
            else:
                years_dict.update({year.year: [year]})
            
        batches = []
        for key, value in years_dict.items():
            batches.append(BatchByYear(key, value))
        return BatchByYearSerializer(batches, many=True).data
























    # def get_batch(self, year):
    #     # batch = Batch.objects.filter(start_date=year)
    #     batch = Batch.objects.all()
    #     # print(batch)
    #     return BatchSerializer(batch, many=True).data
