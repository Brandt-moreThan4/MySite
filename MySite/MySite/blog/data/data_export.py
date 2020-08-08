import csv


DUMP_PATH = r'C:\Users\15314\source\repos\MySite\MySite\blog\data\data_dump'


def export_db(django_model, csv_path=DUMP_PATH):
    """Export the entire django model table to a csv file saved in the data dump folder"""

    all_data = convert_django_model_to_lists(django_model)

    # file name is just the same name as the model. So Book model will be 'Book.csv' 
    csv_path = csv_path + '\\' + django_model.__name__ + '.csv'
    write_to_csv(all_data, csv_path)


def convert_django_model_to_lists(django_model):
    """Takes a django model and returns a list of lists with each inner list containing one row of data associated with the database
    included the column names as the first row."""

    model_fields = [field.name for field in django_model._meta.fields]
    model_data = django_model.objects.all()

    all_data = []
    all_data.append(model_fields) # Column headers

    for row in model_data:
        this_row_data = []
        for field in model_fields:
            field_value = getattr(row, field)
            this_row_data.append(field_value)
        all_data.append(this_row_data)

    return all_data


def write_to_csv(data, csv_destination):
    """Takes an interable of iterables like a list of lists and writes it to the csv
    in the path specificed in csv_destination"""

    with open(csv_destination, 'w', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerows(data)

