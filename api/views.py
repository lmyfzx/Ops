from rest_framework import viewsets, permissions
from api.serializers import *
from assets.models import *
from task.models import *


class InventoryViewSet(viewsets.ModelViewSet):
    """
    处理  GET POST , 处理 /api/post/<pk>/ GET PUT PATCH DELETE
    """
    queryset = AnsibleInventory.objects.all().order_by('id')
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class RunModuleLogViewSet(viewsets.ModelViewSet):
    queryset = AnsibleModuleLog.objects.all().order_by('id')
    serializer_class = ModuleLogSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AssetsViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all().order_by('id')
    serializer_class = AssetsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ServerAssetsViewSet(viewsets.ModelViewSet):
    queryset = ServerAssets.objects.all().order_by('id')
    serializer_class = ServerAssetsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class NetworkAssetsViewSet(viewsets.ModelViewSet):
    queryset = NetworkAssets.objects.all().order_by('id')
    serializer_class = NetworkAssetsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class OfficeAssetsViewSet(viewsets.ModelViewSet):
    queryset = OfficeAssets.objects.all().order_by('id')
    serializer_class = OfficeAssetsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SecurityAssetsViewSet(viewsets.ModelViewSet):
    queryset = SecurityAssets.objects.all().order_by('id')
    serializer_class = SecurityAssetsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class StorageAssetsViewSet(viewsets.ModelViewSet):
    queryset = StorageAssets.objects.all().order_by('id')
    serializer_class = StorageAssetsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SoftwareAssetsViewSet(viewsets.ModelViewSet):
    queryset = SoftwareAssets.objects.all().order_by('id')
    serializer_class = SoftwareAssetsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AssetProviderViewSet(viewsets.ModelViewSet):
    queryset = AssetProvider.objects.all().order_by('id')
    serializer_class = AssetProviderSerializer
    permission_classes = (permissions.IsAuthenticated,)


class IDCViewSet(viewsets.ModelViewSet):
    queryset = IDC.objects.all().order_by('id')
    serializer_class = IDCSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all().order_by('id')
    serializer_class = CabinetSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all().order_by('id')
    serializer_class = PermissionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserLogViewSet(viewsets.ModelViewSet):
    queryset = UserLog.objects.all().order_by('id')
    serializer_class = UserLogSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AssetsLogViewSet(viewsets.ModelViewSet):
    queryset = AssetsLog.objects.all().order_by('id')
    serializer_class = AssetsLogSerializer
    permission_classes = (permissions.IsAuthenticated,)