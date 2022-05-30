namespace CSharpCallPython
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.btn_start = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.txt_py = new System.Windows.Forms.TextBox();
            this.txt_url = new System.Windows.Forms.TextBox();
            this.lbl_py = new System.Windows.Forms.Label();
            this.chk_txt = new System.Windows.Forms.CheckBox();
            this.lbl_url = new System.Windows.Forms.Label();
            this.lbl_state = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // btn_start
            // 
            this.btn_start.Font = new System.Drawing.Font("微软雅黑", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.btn_start.Location = new System.Drawing.Point(15, 25);
            this.btn_start.Margin = new System.Windows.Forms.Padding(4);
            this.btn_start.Name = "btn_start";
            this.btn_start.Size = new System.Drawing.Size(147, 93);
            this.btn_start.TabIndex = 0;
            this.btn_start.Text = "开始爬取";
            this.btn_start.UseVisualStyleBackColor = true;
            this.btn_start.Click += new System.EventHandler(this.button1_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox1.Controls.Add(this.txt_py);
            this.groupBox1.Controls.Add(this.txt_url);
            this.groupBox1.Controls.Add(this.lbl_py);
            this.groupBox1.Controls.Add(this.chk_txt);
            this.groupBox1.Controls.Add(this.lbl_url);
            this.groupBox1.Location = new System.Drawing.Point(13, 13);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(4);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(4);
            this.groupBox1.Size = new System.Drawing.Size(533, 396);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            // 
            // txt_py
            // 
            this.txt_py.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txt_py.Location = new System.Drawing.Point(12, 217);
            this.txt_py.Margin = new System.Windows.Forms.Padding(4);
            this.txt_py.Multiline = true;
            this.txt_py.Name = "txt_py";
            this.txt_py.Size = new System.Drawing.Size(512, 69);
            this.txt_py.TabIndex = 9;
            this.txt_py.TextChanged += new System.EventHandler(this.txt_py_TextChanged);
            // 
            // txt_url
            // 
            this.txt_url.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txt_url.Location = new System.Drawing.Point(12, 81);
            this.txt_url.Margin = new System.Windows.Forms.Padding(4);
            this.txt_url.Multiline = true;
            this.txt_url.Name = "txt_url";
            this.txt_url.Size = new System.Drawing.Size(512, 69);
            this.txt_url.TabIndex = 8;
            this.txt_url.TextChanged += new System.EventHandler(this.txt_url_TextChanged);
            // 
            // lbl_py
            // 
            this.lbl_py.AutoSize = true;
            this.lbl_py.Font = new System.Drawing.Font("微软雅黑", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.lbl_py.Location = new System.Drawing.Point(9, 171);
            this.lbl_py.Name = "lbl_py";
            this.lbl_py.Size = new System.Drawing.Size(217, 27);
            this.lbl_py.TabIndex = 6;
            this.lbl_py.Text = "本地python.exe地址：";
            // 
            // chk_txt
            // 
            this.chk_txt.AutoSize = true;
            this.chk_txt.Location = new System.Drawing.Point(14, 335);
            this.chk_txt.Name = "chk_txt";
            this.chk_txt.Size = new System.Drawing.Size(149, 19);
            this.chk_txt.TabIndex = 4;
            this.chk_txt.Text = "是否爬取文本内容";
            this.chk_txt.UseVisualStyleBackColor = true;
            // 
            // lbl_url
            // 
            this.lbl_url.AutoSize = true;
            this.lbl_url.Font = new System.Drawing.Font("微软雅黑", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.lbl_url.Location = new System.Drawing.Point(9, 40);
            this.lbl_url.Name = "lbl_url";
            this.lbl_url.Size = new System.Drawing.Size(112, 27);
            this.lbl_url.TabIndex = 5;
            this.lbl_url.Text = "网页网址：";
            // 
            // lbl_state
            // 
            this.lbl_state.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lbl_state.Font = new System.Drawing.Font("微软雅黑", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.lbl_state.Location = new System.Drawing.Point(173, 40);
            this.lbl_state.Name = "lbl_state";
            this.lbl_state.Size = new System.Drawing.Size(354, 50);
            this.lbl_state.TabIndex = 2;
            this.lbl_state.Text = "请输入相关参数，\r\n点击开始爬取按钮开始运行。";
            // 
            // groupBox2
            // 
            this.groupBox2.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox2.Controls.Add(this.lbl_state);
            this.groupBox2.Controls.Add(this.btn_start);
            this.groupBox2.Location = new System.Drawing.Point(13, 439);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(533, 125);
            this.groupBox2.TabIndex = 3;
            this.groupBox2.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(565, 617);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "爬取百度文库";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btn_start;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.CheckBox chk_txt;
        private System.Windows.Forms.Label lbl_url;
        private System.Windows.Forms.Label lbl_py;
        private System.Windows.Forms.TextBox txt_url;
        private System.Windows.Forms.Label lbl_state;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.TextBox txt_py;
    }
}

