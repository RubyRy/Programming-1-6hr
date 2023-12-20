require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label1.Location = System::Drawing::Point.new(12, 51)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(166, 38)
		@label1.TabIndex = 0
		@label1.Text = "Radius:"
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(12, 282)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(160, 39)
		@button1.TabIndex = 2
		@button1.Text = "Calculate "
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.BackColor = System::Drawing::Color.Thistle
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(225, 48)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(279, 38)
		@textBox1.TabIndex = 3
		# 
		# button2
		# 
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(178, 282)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(160, 39)
		@button2.TabIndex = 4
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(344, 282)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(160, 39)
		@button3.TabIndex = 5
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.Thistle
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label2.Location = System::Drawing::Point.new(12, 120)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(492, 38)
		@label2.TabIndex = 6
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.Thistle
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label3.Location = System::Drawing::Point.new(12, 175)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(492, 38)
		@label3.TabIndex = 7
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.Thistle
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label4.Location = System::Drawing::Point.new(12, 228)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(492, 38)
		@label4.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.DarkViolet
		self.ClientSize = System::Drawing::Size.new(526, 333)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		Radius = float(@textBox1.Text)
		pi = 3.14159
		area = pi * Radius**2
		area = round(area, 3)
		circ = 2 * pi * Radius
		circ = round(area, 3) 
		@label2.Text = "Area: " + str(area)
		@label3.Text = "Circumfrence: " +str(circ)
		@label4.Text = "Radius: " + str(Radius)
		
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

