from django.views.generic import TemplateView
import quantumrandom
import random


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        try:
            1 / 0  # just for raise a Error for working except section . this try section get two list of Quantumic number in web
            # q_rand_01 = quantumrandom.get_data(data_type='uint16', array_length=15)
            # q_rand_02 = quantumrandom.get_data(data_type='uint16', array_length=15)
        except:
            q_rand_01 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
            q_rand_02 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
            random.shuffle(q_rand_01)
            random.shuffle(q_rand_02)
        # print(q_rand_01,q_rand_02)
        context['q_rand_01'] = q_rand_01
        context['q_rand_02'] = q_rand_02
        return context
