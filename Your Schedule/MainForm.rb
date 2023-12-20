require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.MediumSlateBlue
		@label1.Font = System::Drawing::Font.new("Monotype Corsiva", 24, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label1.Location = System::Drawing::Point.new(29, 19)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(824, 294)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.MediumPurple
		@button1.Font = System::Drawing::Font.new("Monotype Corsiva", 20.25, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@button1.Location = System::Drawing::Point.new(29, 333)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(360, 75)
		@button1.TabIndex = 1
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.MediumPurple
		@button2.Font = System::Drawing::Font.new("Monotype Corsiva", 20.25, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@button2.Location = System::Drawing::Point.new(479, 333)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(374, 75)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.BlueViolet
		self.ClientSize = System::Drawing::Size.new(891, 436)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Your Schedule"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Algebra 1 Honors\n Biology Honors\n English 9 Honors\n Freshman Seminar\n Drawing 1\n Computer Programming 1\n Concer Band\n Global Studies\n"
	end

	def Button2Click(sender, e)
		@labrl1.Text = ""
	end
end

