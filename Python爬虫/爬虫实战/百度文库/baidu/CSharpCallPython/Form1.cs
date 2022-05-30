using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using IronPython.Hosting;
using Microsoft.Scripting;
using Microsoft.Scripting.Hosting;

namespace CSharpCallPython
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private string py = "python.exe";
        //0表示失败，1表示成功
        static private string result = "0";

        private void button1_Click(object sender, EventArgs e)
        {
            string url = txt_url.Text;
            string istxt = "0";
            if (chk_txt.Checked)
                istxt = "1";

            if (!url.Contains("https://wenku.baidu.com/view/"))
            {
                MessageBox.Show("请输入正确的百度文库网址！");
                lbl_state.Text = "请重新输入。";
            }
            else if (!py.Contains("python.exe"))
            {
                MessageBox.Show("请输入正确的python.exe路径！");
                lbl_state.Text = "请重新输入。";
            }
            else
            {
                //输入参数列表
                String[] strArr = new String[] { url, istxt };
                string sArguments = @"src\wenku.py";//这里是python的文件名字
                RunPythonScript(sArguments, py, "-u", strArr);
                if(result.Contains("0"))
                    lbl_state.Text = "对不起，爬取失败。";
                else if (result.Contains("1"))
                    lbl_state.Text = "爬取成功！";
            }
        }

        public static void RunPythonScript(string sArgName, string py, string args = "", params string[] teps)
        {
            Process p = new Process();

            //(没放debug下，写绝对路径)
            //string path = @"C:\Users\zll\Desktop\baidu\CSharpCallPython\bin\Debug\" + sArgName;
            // 获得python文件的绝对路径（将文件放在c#的debug文件夹中可以这样操作）
            string path = System.AppDomain.CurrentDomain.SetupInformation.ApplicationBase + sArgName;

            //没有配环境变量的话，可以像我这样写python.exe的绝对路径。如果配了，直接写"python.exe"即可
            //p.StartInfo.FileName = @"C:\Users\zll\AppData\Local\Programs\Python\Python37-32\python.exe";
            p.StartInfo.FileName = @py;
            string sArguments = path;

            foreach (string sigstr in teps)
            {
                sArguments += " " + sigstr;//传递参数
            }

            sArguments += " " + args;

            p.StartInfo.Arguments = sArguments;
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;

            p.Start();
            p.BeginOutputReadLine();
            p.OutputDataReceived += new DataReceivedEventHandler(p_OutputDataReceived);
            Console.ReadLine();
            p.WaitForExit();
        }
        //输出打印的信息
        static void p_OutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            if (!string.IsNullOrEmpty(e.Data))
            {
                AppendText(e.Data + Environment.NewLine);
            }
        }
        public delegate void AppendTextCallback(string text);
        public static void AppendText(string text)
        {
            Console.WriteLine(text);     //此处在控制台输出.py文件print的结果
            result = text;
        }

        private void txt_py_TextChanged(object sender, EventArgs e)
        {
            py = txt_py.Text;
        }

        private void txt_url_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
