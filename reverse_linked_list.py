from manim import *

class ReverseLinkedList(Scene):
    def construct(self):
        # Values in the linked list
        values = ["1", "2", "3", "4"]

        # Create boxes for each node
        nodes = [Square(side_length=1).set_fill(WHITE, opacity=0.9) for _ in values]
        labels = [Text(val, color=BLACK).scale(0.6) for val in values]

        # Position the nodes
        for i, node in enumerate(nodes):
            node.move_to(RIGHT * i * 2)

        # Add labels inside the nodes
        for node, label in zip(nodes, labels):
            label.move_to(node.get_center())

        # Create arrows between nodes
        arrows = []
        for i in range(len(nodes) - 1):
            arrow = Arrow(nodes[i].get_right(), nodes[i + 1].get_left(), buff=0.1)
            arrows.append(arrow)

        # Add pointer labels
        prev_label = Text("prev", color=BLUE).scale(0.5)
        current_label = Text("current", color=GREEN).scale(0.5)
        next_label = Text("next_node", color=RED).scale(0.5)

        # Position labels
        prev_label.next_to(nodes[0], UP, buff=1.2).shift(LEFT * 2)
        current_label.next_to(nodes[0], UP, buff=1.2)
        next_label.next_to(nodes[1], UP, buff=1.2)

        self.play(Write(prev_label), Write(current_label), Write(next_label))
        self.wait(1)

        # Step 1: Reverse pointer from node 1 to None (no visible arrow yet)
        reverse_arrow = Arrow(nodes[1].get_left(), nodes[0].get_right(), buff=0.1)
        self.play(FadeOut(arrows[0]), GrowArrow(reverse_arrow))
        self.wait(1)

        # Step 2: Move prev to node 1, current to node 2
        self.play(
            prev_label.animate.next_to(nodes[0], UP, buff=1.2),
            current_label.animate.next_to(nodes[1], UP, buff=1.2),
            next_label.animate.next_to(nodes[2], UP, buff=1.2)
        )
        self.wait(2)

        # Add everything to the scene
        self.play(*[FadeIn(node) for node in nodes], *[Write(label) for label in labels])
        self.wait(0.5)
        self.play(*[GrowArrow(arrow) for arrow in arrows])
        self.wait(1)