﻿require "mscorlib"
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
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@label4 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label1.Location = System::Drawing::Point.new(12, 25)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(155, 53)
		@label1.TabIndex = 0
		@label1.Text = "Length:"
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label2.Location = System::Drawing::Point.new(12, 84)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(155, 53)
		@label2.TabIndex = 4
		@label2.Text = "Width:"
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.Thistle
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(12, 142)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(447, 53)
		@label3.TabIndex = 5
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.MediumOrchid
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@button1.Location = System::Drawing::Point.new(12, 360)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(144, 53)
		@button1.TabIndex = 6
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.MediumOrchid
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@button2.Location = System::Drawing::Point.new(174, 360)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(130, 53)
		@button2.TabIndex = 7
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.MediumOrchid
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@button3.Location = System::Drawing::Point.new(329, 360)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(130, 53)
		@button3.TabIndex = 8
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(174, 22)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(285, 38)
		@textBox1.TabIndex = 9
		# 
		# textBox2
		# 
		@textBox2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(174, 81)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(285, 38)
		@textBox2.TabIndex = 10
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.Thistle
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(12, 210)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(447, 53)
		@label4.TabIndex = 11
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.DarkOrchid
		self.ClientSize = System::Drawing::Size.new(492, 453)
		self.Controls.Add(@label4)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Prog52a"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		length = int(@textBox1.Text)
		width = int(@textBox2.Text)
		area = length * width
		perim = 2 * length + 2 * width
		@label3.Text = "Area: " + str(area)
		@label4.Text = "Perimeter: " + str(perim)
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@texBox2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

