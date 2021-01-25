from django.shortcuts import render, redirect
from .models import Vendor
from .forms import VendorForm
from django.contrib.auth.decorators import login_required
from tablib import Dataset

# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')


@login_required
def vendor_list(request):
    # select all vendor objects from the DB into a QuerySet
    all_vendors = Vendor.objects.all()
    # order by alphabet
    sorted_vendors = all_vendors.order_by('name')
    # render templates
    return render(request, 'vendor_list.html', {'vendors': sorted_vendors})


@login_required
def vendor_detail(request, pk):
    vendor_info = Vendor.objects.get(id=pk)
    return render(request, 'vendor_detail.html', {'vendor': vendor_info})


@login_required
def vendor_create(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = VendorForm()
    return render(request, 'vendor_form.html', {'form': form})


@login_required
def vendor_edit(request, pk):
    vendor = Vendor.objects.get(pk=pk)
    if request.method == "POST":
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            vendor = form.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'vendor_form.html', {'form': form})


@login_required
def vendor_delete(request, pk):
    Vendor.objects.get(id=pk).delete()
    return redirect('vendor_list')


def simple_upload(request):
    if request.method == 'POST':
        vendor_resource = VendorResource()
        dataset = Dataset()
        new_vendors = request.FILES['myfile']

        imported_data = dataset.load(new_vendors.read())
        result = vendor_resource.import_data(
            dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            vendor_resource.import_data(
                dataset, dry_run=False)  # Actually import now

    return render(request, 'vendor_list.html')
