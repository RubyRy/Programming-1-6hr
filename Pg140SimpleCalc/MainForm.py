import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.CadetBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(3, 34)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(52, 39)
		self._label1.TabIndex = 0
		self._label1.Text = "#:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.CadetBlue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(3, 142)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(52, 39)
		self._label3.TabIndex = 2
		self._label3.Text = "#:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.CadetBlue
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(3, 259)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(52, 39)
		self._label4.TabIndex = 3
		self._label4.Text = "="
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.CadetBlue
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(61, 259)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(292, 39)
		self._label6.TabIndex = 5
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(227, 92)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(38, 36)
		self._button1.TabIndex = 6
		self._button1.Text = "/"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(227, 38)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(38, 36)
		self._button2.TabIndex = 7
		self._button2.Text = "+"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(271, 38)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(38, 36)
		self._button3.TabIndex = 8
		self._button3.Text = "-"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(315, 38)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(38, 36)
		self._button4.TabIndex = 9
		self._button4.Text = "*"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(271, 92)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(38, 36)
		self._button5.TabIndex = 10
		self._button5.Text = "//"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(315, 92)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(38, 36)
		self._button6.TabIndex = 11
		self._button6.Text = "^"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(254, 138)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(83, 36)
		self._button7.TabIndex = 12
		self._button7.Text = "MOD"
		self._button7.UseVisualStyleBackColor = True
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(245, 178)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(92, 36)
		self._button8.TabIndex = 13
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(245, 220)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(92, 36)
		self._button9.TabIndex = 14
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = True
		self._button9.Click += self.Button9Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(75, 34)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(146, 40)
		self._textBox1.TabIndex = 15
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(75, 138)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(146, 40)
		self._textBox2.TabIndex = 16
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.CadetBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(96, 89)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(99, 39)
		self._label2.TabIndex = 17
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SlateGray
		self.ClientSize = System.Drawing.Size(365, 307)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg140SimpleCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		e = float(self._textBox1.Text) + float(self._textBox2.Text)
		self._label2.Text = "+"
		self._label6.Text = str(e)
		
		
		

	def Button3Click(self, sender, e):
		l = float(self._textBox1.Text) - float(self._textBox2.Text)
		self._label2.Text = "-"
		self._label6.Text = str(l)

	def Button4Click(self, sender, e):
		m = float(self._textBox1.Text) * float(self._textBox2.Text)
		self._label2.Text = "*"
		self._label6.Text = str(m)

	def Button1Click(self, sender, e):
		d = float(self._textBox1.Text) / float(self._textBox2.Text)
		self._label2.Text = "/"
		self._label6.Text = str(round(d, 3))

	def Button5Click(self, sender, e):
		u = float(self._textBox1.Text) // float(self._textBox2.Text)
		self._label2.Text = "//"
		self._label6.Text = str(u)

	def Button6Click(self, sender, e):
		r = float(self._textBox1.Text) ** float(self._textBox2.Text)
		self._label2.Text = "**"
		self._label6.Text = str(r)

	def Button7Click(self, sender, e):
		j =float(self._textBox1.Text) % float(self._textBox2.Text)
		self._label2.Text = "MOD"
		self._label6.Text =  str(j)

	def Button8Click(self, sender, e):
		self._label2.Text = " "
		self._label6.Text = " "
		self._textBox1.Clear()
		self._textBox2.Clear()

	def Button9Click(self, sender, e):
		Application.Exit()