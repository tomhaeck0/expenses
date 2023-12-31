from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import csv
from io import TextIOWrapper

from expense_tracker.models import Transfer

from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.embed import components

from expense_tracker.forms import TransferUploadForm
from expense_tracker.models import Transfer


def create_graph():

    p = figure(title="My Bokeh Plot",
                 x_axis_label="X-axis",
                 y_axis_label="Y-axis",
                )
    p.line([1, 2, 3, 5, 5], [6, 7, 8, 9, 10], line_width=2)

    script, div = components(p)
    return script, div


def create_bars(data):
    # Create a Bokeh figure
    p = figure(x_range=[str(i) for i in range(len(data))], title="Vertical Bar Plot")

    # Create vertical bars using vbar
    p.vbar(x=[str(i) for i in range(len(data))], top=data, width=0.5, color="navy")

    # Customize the plot
    p.xaxis.axis_label = "X-Axis Label"
    p.yaxis.axis_label = "Y-Axis Label"

    # Show the plot
    script, div = components(p)
    return script, div


# Create your views here.
def view_prototype(request):
    transfers = Transfer.objects.all()
    print(len(transfers))

    data = [transfer.amount for transfer in transfers]

    script, div = create_bars(data)
    return render(request, 'expense_tracker/bokeh_template.html', {'script': script, 'div': div})


def upload_transfers(request):
    if request.method == 'POST':
        form = TransferUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.cleaned_data['transfer_file']

            if not uploaded_file.content_type == 'text/csv':
                raise ValueError('Uploaded file is not a csv file.')

            #import csv
            with TextIOWrapper(uploaded_file.file, encoding='UTF-8') as csv_file:
                transfers = Transfer.transfers_from_csv(csv_file)

            for transfer in transfers:
                print(transfer)

            return HttpResponseRedirect('/success/')

    else:
        form = TransferUploadForm()

    return render(request, 'expense_tracker/upload_transfers.html', {'form': form})
