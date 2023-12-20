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
		@textBox1 = System::Windows::Forms::TextBox.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@label6 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(12, 31)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(136, 39)
		@label1.TabIndex = 0
		@label1.Text = "Number1:"
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(154, 32)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(236, 38)
		@textBox1.TabIndex = 1
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(12, 383)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(136, 37)
		@button1.TabIndex = 2
		@button1.Text = "Caculate "
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(154, 383)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(108, 37)
		@button2.TabIndex = 3
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(268, 383)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(122, 37)
		@button3.TabIndex = 4
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.SlateGray
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.ForeColor = System::Drawing::Color.Transparent
		@label2.Location = System::Drawing::Point.new(12, 268)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(378, 39)
		@label2.TabIndex = 5
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.SlateGray
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.ForeColor = System::Drawing::Color.Transparent
		@label3.Location = System::Drawing::Point.new(12, 317)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(378, 39)
		@label3.TabIndex = 6
		# 
		# textBox2
		# 
		@textBox2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(154, 88)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(236, 38)
		@textBox2.TabIndex = 7
		# 
		# textBox3
		# 
		@textBox3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox3.Location = System::Drawing::Point.new(154, 149)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(236, 38)
		@textBox3.TabIndex = 8
		# 
		# textBox4
		# 
		@textBox4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox4.Location = System::Drawing::Point.new(154, 202)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(236, 38)
		@textBox4.TabIndex = 9
		# 
		# label4
		# 
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(12, 87)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(136, 39)
		@label4.TabIndex = 10
		@label4.Text = "Number2:"
		# 
		# label5
		# 
		@label5.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(12, 149)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(136, 39)
		@label5.TabIndex = 11
		@label5.Text = "Number3:"
		# 
		# label6
		# 
		@label6.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label6.Location = System::Drawing::Point.new(12, 201)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(136, 39)
		@label6.TabIndex = 12
		@label6.Text = "Number4:"
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.CornflowerBlue
		self.ClientSize = System::Drawing::Size.new(420, 450)
		self.Controls.Add(@label6)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Label1Click(sender, e)
		
	end

	def Button1Click(sender, e)
		Number1 = int(@textBox1.Text)
		Number2 = int(@textBox2.Text)
		Number3 = int(@textBox3.Text)
		Number4 = int(@textBox3.Text)
		Sum = Number1 + Number2 + Number3 + Number4
		Avg = Sum / 4.0
		@label2.Text = "Sum: " + str(Sum)
		@label3.Text = "Average: " + str(Avg)
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
		@label2.Text = ""
		@label3.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

