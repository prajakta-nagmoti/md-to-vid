from manim import *

# Clean educational style constants.
BG_COLOR = "#F7F9FC"
PRIMARY = "#1E3A5F"
ACCENT = "#0E9F6E"
WARN = "#C2410C"
TEXT_DARK = "#111827"
MUTED = "#4B5563"


class LLMTitleScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("Large Language Models (LLMs)", color=PRIMARY, weight=BOLD).scale(0.9)
        subtitle = Text(
            "Neural networks trained on massive text corpora to predict the next token",
            color=MUTED,
        ).scale(0.45)
        subtitle.next_to(title, DOWN, buff=0.35)

        frame = RoundedRectangle(
            corner_radius=0.2,
            width=12.2,
            height=2.8,
            stroke_color=PRIMARY,
            stroke_width=2,
            fill_opacity=0.0,
        )
        frame.move_to((title.get_center() + subtitle.get_center()) / 2)

        self.play(FadeIn(frame, scale=0.98), run_time=0.9)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(subtitle, shift=0.15 * UP), run_time=1.1)
        self.wait(1.1)
        self.play(FadeOut(VGroup(frame, title, subtitle)), run_time=0.8)


class HowTheyWorkScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        heading = Text("How They Work", color=PRIMARY, weight=BOLD).scale(0.72).to_edge(UP)

        token_boxes = VGroup(*[
            RoundedRectangle(width=1.6, height=0.8, corner_radius=0.12, stroke_color=PRIMARY, fill_color=WHITE, fill_opacity=1)
            for _ in range(4)
        ]).arrange(RIGHT, buff=0.3).shift(UP * 1.4)

        labels = ["Input", "is", "tokenized", "..."]
        token_text = VGroup(*[
            Text(labels[i], color=TEXT_DARK).scale(0.38).move_to(token_boxes[i].get_center())
            for i in range(4)
        ])

        transformer = RoundedRectangle(
            width=5.2,
            height=1.1,
            corner_radius=0.15,
            stroke_color=ACCENT,
            fill_color="#E8F8F0",
            fill_opacity=1,
        ).shift(DOWN * 0.1)
        transformer_label = Text("Transformer + Attention", color=ACCENT, weight=BOLD).scale(0.45).move_to(transformer)

        arrow_down = Arrow(token_boxes.get_bottom(), transformer.get_top(), buff=0.2, color=MUTED, stroke_width=4)

        output_tokens = VGroup(*[
            RoundedRectangle(width=1.5, height=0.7, corner_radius=0.1, stroke_color=PRIMARY, fill_color=WHITE, fill_opacity=1)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.25).shift(DOWN * 1.8)
        out_texts = ["next", "token", "..."]
        output_labels = VGroup(*[
            Text(out_texts[i], color=TEXT_DARK).scale(0.36).move_to(output_tokens[i].get_center())
            for i in range(3)
        ])

        arrow_out = Arrow(transformer.get_bottom(), output_tokens.get_top(), buff=0.2, color=MUTED, stroke_width=4)

        bullet_1 = Text("1. Split text into tokens", color=TEXT_DARK).scale(0.4).to_edge(LEFT).shift(DOWN * 2.9)
        bullet_2 = Text("2. Model learns token relationships", color=TEXT_DARK).scale(0.4).next_to(bullet_1, RIGHT, buff=0.45)
        bullet_3 = Text("3. Predict next token repeatedly", color=TEXT_DARK).scale(0.4).next_to(bullet_2, RIGHT, buff=0.45)

        self.play(FadeIn(heading, shift=0.2 * DOWN), run_time=0.7)
        self.play(LaggedStart(*[Create(b) for b in token_boxes], lag_ratio=0.12), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(t, shift=0.1 * UP) for t in token_text], lag_ratio=0.1), run_time=0.9)
        self.play(GrowArrow(arrow_down), FadeIn(transformer), FadeIn(transformer_label), run_time=1.0)
        self.play(GrowArrow(arrow_out), LaggedStart(*[Create(o) for o in output_tokens], lag_ratio=0.1), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(t, shift=0.05 * UP) for t in output_labels], lag_ratio=0.1), run_time=0.8)
        self.play(FadeIn(VGroup(bullet_1, bullet_2, bullet_3), shift=0.2 * UP), run_time=1.0)
        self.wait(1.1)


class WhyTheyMatterScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        heading = Text("Why They Matter", color=PRIMARY, weight=BOLD).scale(0.72).to_edge(UP)
        self.play(FadeIn(heading, shift=0.2 * DOWN), run_time=0.7)

        cards_data = [
            ("Summarize", "Turn long text into concise insights"),
            ("Explain", "Break down difficult topics quickly"),
            ("Translate", "Bridge language barriers"),
            ("Generate Code", "Accelerate software workflows"),
        ]

        cards = VGroup()
        for title, desc in cards_data:
            card = RoundedRectangle(
                width=5.5,
                height=1.4,
                corner_radius=0.12,
                stroke_color=PRIMARY,
                fill_color=WHITE,
                fill_opacity=1,
            )
            t = Text(title, color=PRIMARY, weight=BOLD).scale(0.45).move_to(card.get_center() + UP * 0.25)
            d = Text(desc, color=MUTED).scale(0.31).move_to(card.get_center() + DOWN * 0.26)
            cards.add(VGroup(card, t, d))

        cards.arrange_in_grid(rows=2, cols=2, buff=0.35).shift(DOWN * 0.4)

        productivity = Text("Result: Better writing + faster software delivery", color=ACCENT, weight=BOLD).scale(0.46)
        productivity.next_to(cards, DOWN, buff=0.6)

        self.play(LaggedStart(*[FadeIn(c, shift=0.15 * UP) for c in cards], lag_ratio=0.12), run_time=1.4)
        self.play(Write(productivity), run_time=1.0)
        self.wait(1.1)


class KeyLimitsScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        heading = Text("Key Limits", color=WARN, weight=BOLD).scale(0.72).to_edge(UP)
        self.play(FadeIn(heading, shift=0.2 * DOWN), run_time=0.7)

        limits = [
            "Can hallucinate incorrect facts",
            "Output quality depends on prompt clarity and context",
            "Critical tasks require human validation",
        ]

        rows = VGroup()
        for item in limits:
            dot = Dot(radius=0.07, color=WARN)
            txt = Text(item, color=TEXT_DARK).scale(0.42)
            row = VGroup(dot, txt).arrange(RIGHT, buff=0.25, aligned_edge=UP)
            rows.add(row)

        rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT).shift(UP * 0.1)
        rows.move_to(ORIGIN)

        caution_box = RoundedRectangle(
            width=10.8,
            height=3.2,
            corner_radius=0.18,
            stroke_color=WARN,
            stroke_width=2,
            fill_color="#FFF7ED",
            fill_opacity=1,
        )
        caution_box.move_to(rows.get_center())

        self.play(FadeIn(caution_box), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(r, shift=0.2 * RIGHT) for r in rows], lag_ratio=0.2), run_time=1.6)
        self.wait(1.1)


class SafeUseTipsScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        heading = Text("Safe Use Tips", color=ACCENT, weight=BOLD).scale(0.72).to_edge(UP)
        self.play(FadeIn(heading, shift=0.2 * DOWN), run_time=0.7)

        steps = [
            "Ask for sources or reasoning steps",
            "Verify important claims independently",
            "Keep humans in the loop for final decisions",
        ]

        ladder = VGroup()
        for i, s in enumerate(steps, start=1):
            badge = Circle(radius=0.22, color=ACCENT, fill_color="#E8F8F0", fill_opacity=1)
            num = Text(str(i), color=ACCENT, weight=BOLD).scale(0.4).move_to(badge)
            txt = Text(s, color=TEXT_DARK).scale(0.42)
            row = VGroup(VGroup(badge, num), txt).arrange(RIGHT, buff=0.35)
            ladder.add(row)

        ladder.arrange(DOWN, buff=0.6, aligned_edge=LEFT).shift(DOWN * 0.2)

        connectors = VGroup()
        for i in range(len(ladder) - 1):
            start = ladder[i][0].get_bottom()
            end = ladder[i + 1][0].get_top()
            connectors.add(Line(start, end, color=ACCENT, stroke_width=3))

        wrap = RoundedRectangle(
            width=11.3,
            height=4.6,
            corner_radius=0.2,
            stroke_color=ACCENT,
            fill_opacity=0,
            stroke_width=2,
        )
        wrap.move_to(ladder.get_center())

        closing = Text("Use LLMs as assistants, not final authorities.", color=PRIMARY, weight=BOLD).scale(0.45)
        closing.next_to(wrap, DOWN, buff=0.45)

        self.play(Create(wrap), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(l, shift=0.15 * RIGHT) for l in ladder], lag_ratio=0.25), run_time=1.5)
        self.play(LaggedStart(*[Create(c) for c in connectors], lag_ratio=0.2), run_time=0.8)
        self.play(Write(closing), run_time=1.0)
        self.wait(1.2)


class LLMCompleteLessonScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # Slide 1: Title + definition
        title = Text("Large Language Models", color=PRIMARY, weight=BOLD).scale(0.95).to_edge(UP)
        definition = Text(
            "Neural networks trained on massive text to predict the next token",
            color=MUTED,
        ).scale(0.43).next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(title, shift=0.2 * DOWN), FadeIn(definition, shift=0.2 * UP), run_time=1.1)
        self.wait(0.7)

        # Slide 2: How they work
        work_box = RoundedRectangle(
            width=11,
            height=2.4,
            corner_radius=0.18,
            stroke_color=PRIMARY,
            fill_color=WHITE,
            fill_opacity=1,
        ).shift(UP * 0.45)
        steps = VGroup(
            Text("1) Tokenize input", color=TEXT_DARK).scale(0.44),
            Text("2) Transformer attends to token relationships", color=TEXT_DARK).scale(0.44),
            Text("3) Predict next token repeatedly", color=TEXT_DARK).scale(0.44),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT).move_to(work_box.get_center())
        self.play(ReplacementTransform(definition, work_box), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(s, shift=0.15 * RIGHT) for s in steps], lag_ratio=0.2), run_time=1.2)
        self.wait(0.8)

        # Slide 3: Why they matter
        matter_title = Text("Why They Matter", color=ACCENT, weight=BOLD).scale(0.58)
        matter_title.next_to(work_box, DOWN, buff=0.55)
        matter_points = VGroup(
            Text("Summarize, explain, translate, and generate code", color=TEXT_DARK).scale(0.4),
            Text("Boost productivity in writing and software workflows", color=TEXT_DARK).scale(0.4),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(matter_title, DOWN, buff=0.25)
        self.play(Write(matter_title), run_time=0.8)
        self.play(FadeIn(matter_points, shift=0.15 * UP), run_time=0.9)
        self.wait(0.8)

        # Slide 4: Limits and safe use
        limits = VGroup(
            Text("Limits: can hallucinate; quality depends on prompt and context", color=WARN).scale(0.4),
            Text("Safe use: ask for sources, verify claims, keep humans in the loop", color=ACCENT).scale(0.4),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).to_edge(DOWN).shift(UP * 0.7)

        divider = Line(LEFT * 5.6, RIGHT * 5.6, color="#D1D5DB", stroke_width=2).next_to(matter_points, DOWN, buff=0.5)
        self.play(Create(divider), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(l, shift=0.2 * RIGHT) for l in limits], lag_ratio=0.25), run_time=1.3)
        self.wait(1.0)

        outro = Text("Use LLMs as capable assistants, not final authorities.", color=PRIMARY, weight=BOLD).scale(0.46)
        outro.to_edge(DOWN).shift(UP * 0.2)
        self.play(Write(outro), run_time=0.9)
        self.wait(1.0)
