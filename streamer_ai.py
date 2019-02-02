from manim import *
from network import NeuralNetworkMobject


class Intro(Scene):
    def construct(self):
        title = TextMobject("Super Mario NEAT")
        title.scale(1.5)
        title.to_edge(UP)
        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)
        self.play(
            FadeInFromDown(title),
            ShowCreation(rect)
        )
        self.wait(2)


class InputANN(Scene):
    def construct(self):
        mario = SVGMobject("files/mario.svg")
        a = Arrow(LEFT, RIGHT, color=RED)

        nn = SVGMobject("files/nn.svg")
        nn.move_to(2.5 * RIGHT)

        head = TextMobject("Artificial Neural Network", color=BLUE)
        head.move_to(2 * UP)
        head.scale(1.5)

        foot = TextMobject("Recommender System", color=RED)
        foot.move_to(2 * DOWN)
        foot.scale(1.5)

        self.play(ShowCreation(mario))
        self.play(ApplyMethod(mario.shift, 2.5 * LEFT), ShowCreation(a))
        self.play(ShowCreation(nn))
        self.wait(2)

        self.play(ShowCreation(head))
        self.wait(2)

        self.play(ShowCreation(foot))
        self.wait(2)


class NeuralNetwork(Scene):
    def construct(self):
        network = NeuralNetworkMobject([3, 4, 3])
        network.scale(2.5)

        neuron_arrow = Arrow(ORIGIN, 1 * UP)
        neuron_arrow.next_to(network, 1 * UP)

        neuron_text = TextMobject("Neurons")
        neuron_text.next_to(neuron_arrow, 1 * UP)

        input_arrow = Arrow(1 * LEFT, ORIGIN, color=BLUE)
        input_arrow.next_to(network, 2 * LEFT)

        input_text = TextMobject("Inputs", color=BLUE)
        input_text.next_to(input_arrow, 1 * UP)

        output_arrow = Arrow(ORIGIN, 1 * RIGHT, color=RED)
        output_arrow.next_to(network, 2 * RIGHT)

        output_text = TextMobject("Outputs", color=RED)
        output_text.next_to(output_arrow, 1 * UP)

        weight_arrow = Arrow(2 * LEFT, 2 * LEFT + 2 * DOWN)

        weight_text = TextMobject("Weights")
        weight_text.next_to(weight_arrow, 1 * DOWN)

        brace = Brace(VGroup(network), DOWN)
        text = brace.get_text("Bias")

        self.play(ShowCreation(network))
        self.wait(2)

        self.play(ShowCreation(neuron_arrow), ShowCreation(neuron_text))
        self.wait(2)

        self.play(ShowCreation(input_arrow), ShowCreation(input_text))
        self.wait(2)

        self.play(ShowCreation(output_arrow), ShowCreation(output_text))
        self.wait(2)

        self.play(ShowCreation(weight_arrow), ShowCreation(weight_text))
        self.wait(2)

        self.play(ShowCreation(brace), ShowCreation(text))
        self.wait(2)


class Sigmoid(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": 0,
        "y_max": 1,
        "graph_origin": 3 * DOWN,
        "function_color": RED,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2)
    }

    def construct(self):
        text = TextMobject("Sigmoid")
        text.scale(2)
        text.move_to(3 * UP)

        self.setup_axes(animate=True)

        self.play(ApplyMethod(self.axes.scale, 0.75))

        func_graph = self.get_graph(self.sigmoid, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label=r"\sigma (x) = max(x, \alpha x)", color=WHITE)
        graph_lab.scale(0.75)

        brace = Brace(VGroup(func_graph), LEFT)
        b_text = brace.get_tex(r"0 < \sigma (x) < 1")

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_lab))
        self.play(ShowCreation(text))

        self.play(ShowCreation(brace), ShowCreation(b_text))
        self.wait(2)

    def sigmoid(self, x):
        return 1 / (1 + math.e ** (-x))


class Relu(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": GREEN,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2)
    }

    def construct(self):
        text = TextMobject("ReLU")
        text.scale(2)
        text.move_to(3 * UP)

        self.setup_axes(animate=True)

        self.play(ApplyMethod(self.axes.scale, 0.75))

        func_graph = self.get_graph(self.relu, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label=r"y = max(x, \alpha x)")

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_lab))
        self.play(ShowCreation(text))
        self.wait(2)

    @staticmethod
    def relu(x):
        return max(x, 0)


class LeakyRelu(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": BLUE,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2)
    }

    def construct(self):
        text = TextMobject("Leaky ReLU")
        text.scale(2)
        text.move_to(3 * UP)

        self.setup_axes(animate=True)

        self.play(ApplyMethod(self.axes.scale, 0.75))

        func_graph = self.get_graph(self.leaky_relu, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label=r"y = max(x, \alpha x)")

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_lab))
        self.play(ShowCreation(text))
        self.wait(2)

    @staticmethod
    def leaky_relu(x):
        return max(x, x / 4)


class SoftMax(GraphScene):
    def construct(self):
        equation = TexMobject(r"\sigma (x_j) = \frac{e^{x_j}}{\sum _i {e^{x_i}}")
        head = TextMobject("Softmax", color=GREEN)

        equation.scale(2)
        head.scale(2)
        head.move_to(2 * UP)

        self.play(ShowCreation(head))
        self.play(ShowCreation(equation))
        self.wait(2)
