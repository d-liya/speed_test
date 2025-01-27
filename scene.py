from manim import *

class ManimScene(Scene):
      def construct(self):
          # Load images
          globe = ImageMobject("spinning_globe.png")
          sri_lanka = ImageMobject("map.png")
          
          # Scale images appropriately
          globe.scale(3)
          sri_lanka.scale(2)

          # Initial globe animation
          self.play(FadeIn(globe), run_time=1)
          self.play(
              Rotate(globe, angle=TAU, rate_func=linear),
              run_time=4
          )

          # Zoom transition
          self.play(
              globe.animate.scale(1.5),
              run_time=3
          )

          # Transform to Sri Lanka map
          self.play(
              Transform(globe, sri_lanka),
              run_time=4
          )

          # Create pulsing effect
          def create_pulse():
              pulse = Circle(
                  radius=2,
                  stroke_width=2,
                  stroke_color=BLUE,
                  fill_opacity=0
              )
              return pulse

          # Add pulsing animation
          pulses = VGroup(*[create_pulse() for _ in range(3)])
          self.play(
              *[
                  Succession(
                      ShowCreation(pulse),
                      pulse.animate.scale(1.5).set_opacity(0),
                      run_time=2
                  )
                  for pulse in pulses
              ],
              run_time=3
          )

          # Create wave effect
          waves = VGroup()
          num_waves = 8
          for i in range(num_waves):
              wave = ParametricFunction(
                  lambda t: np.array([
                      t,
                      0.5 * np.sin(t + i * PI/4),
                      0
                  ]),
                  t_range=[-3, 3],
                  stroke_color=BLUE_C,
                  stroke_opacity=0.6
              )
              waves.add(wave)

          waves.scale(0.5).next_to(sri_lanka, DOWN, buff=0.5)

          # Animate waves
          self.play(
              ShowCreation(waves),
              *[
                  ApplyMethod(
                      wave.shift, UP * 0.3 * np.sin(i * PI/4),
                      rate_func=there_and_back,
                      run_time=4
                  )
                  for i, wave in enumerate(waves)
              ],
              run_time=4
          )

          self.wait()