#import dependencies
import pandas, numpy, pygal


def overview_genre():
    data_frame = pandas.read_csv('vgsales.csv')
    create_chart(data_frame)

#chart creation
def create_chart(data_frame):
    data = numpy.array(data_frame.groupby('Genre', as_index=False).count()[['Genre', 'Rank']]).tolist()

    chart = pygal.Bar()

    for i in data:
        chart.add(i[0], [{'value': i[1], 'label': '{:.2f}%'.format(100*i[1]/sum([j[1] for j in data]))}])

    chart.legend_at_bottom = True
    chart.legend_box_size = 16
    chart.render_to_file('genre.svg')

overview_genre()