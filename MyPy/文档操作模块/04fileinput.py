import fileinput

f = fileinput.input(files=('a.txt', 'a_copy.txt'))  # input()--�ӿ���̨��ȡ�ļ� FileInput()��һ��ʵ���࣬����ͬ��
print(f.filename())
print(f.fileno())  # �ļ���������δ�򿪣�-1
print(f.lineno())  # ��ȡ���кţ�δ��ȡ��0
print(f.filelineno())  # �ļ��кţ�δ��ȡ��0
print(f.isfirstline())  # �Ƿ��һ��
print(f.isstdin())  # �Ƿ����Կ���̨�ļ�
print(f.nextfile())  # �رյ�ǰ�ļ���ȥ��һ�ļ�
f.close()