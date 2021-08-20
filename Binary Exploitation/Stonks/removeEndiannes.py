from textwrap import wrap
flag = 'ocip{FTC0l_I4_t5m_ll0m_y_y3n2fc10a10ÿ¾}';
groups = wrap(flag, 4);
reverseGroups = [];

for group in groups:
   reverseGroups.append(group[::-1]);

print(''.join(reverseGroups))