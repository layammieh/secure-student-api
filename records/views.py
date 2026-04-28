from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import StudentRecord
from .serializers import StudentRecordSerializer
from .permissions import IsAdmin, IsAdminOrFaculty


class StudentRecordViewSet(ModelViewSet):
    serializer_class = StudentRecordSerializer
    queryset = StudentRecord.objects.all()


    def get_permissions(self):

        # Only admins can create/delete
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAdmin]

        # Faculty + Admin can update
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsAdminOrFaculty]

        # Everyone authenticated can view
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


    # Students see only their own record
    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name='Student').exists():
            return StudentRecord.objects.filter(owner=user)

        return StudentRecord.objects.all()