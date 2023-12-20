import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.Violet
		self._radioButton1.Location = System.Drawing.Point(9, 11)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Choice 1"
		self._radioButton1.UseVisualStyleBackColor = False
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.Color.Violet
		self._checkBox1.Location = System.Drawing.Point(155, 12)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 1
		self._checkBox1.Text = "Choice 4"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.Violet
		self._radioButton2.Location = System.Drawing.Point(9, 41)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 2
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Choice 2"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.Violet
		self._radioButton3.Location = System.Drawing.Point(9, 71)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 3
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Choice 3"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.Color.Violet
		self._checkBox2.Location = System.Drawing.Point(155, 42)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 4
		self._checkBox2.Text = "Choice 5"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.Color.Violet
		self._checkBox3.Location = System.Drawing.Point(155, 72)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 5
		self._checkBox3.Text = "Choice 6"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 101)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(129, 21)
		self._button1.TabIndex = 6
		self._button1.Text = "OK"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(143, 102)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(129, 21)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Thistle
		self.ClientSize = System.Drawing.Size(284, 134)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "Pg247Radio"
		self.ResumeLayout(False)


	def RadioButton1CheckedChanged(self, sender, e):
		pass
	
	def Button1Click(self, sender, e):
		strMessage = " "
		if self._radioButton1.Checked == True:
			strMessage = "You selected Choice 1"
		elif self._radioButton2.Checked == True:
			strMessage = "You selected Choice 2"
		elif self._radioButton3.Checked == True:
			strMessage = "You selected Choice 3"
		if self._checkBox1.Checked == True:
			strMessage += " and Choice 4"
		if self._checkBox2.Checked == True:
			strMessage += " and Choice 5"
		if self._checkBox3.Checked == True:
			strMessage += " and Choice 6"
			
		MessageBox.Show(strMessage)

	def Button2Click(self, sender, e):
		Application.Exit()