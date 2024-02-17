from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    default_serializer = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    serializers_choice = {
        'retrieve': CourseDetailSerializer,
    }

    def get_serializer_class(self):
        """определяем сериализатор с учетом запрашиваемого действия(self.action = list, retrieve, create, update,
        delete). Если действие не указано в словарике serializers_choice - используется default_serializer"""
        return self.serializers_choice.get(self.action, self.default_serializer)


class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonDestroyView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
