for i in range(1, 22):
    f = open('{}.tex'.format(i), 'w')
    f.write('\section{}\n\n\subsection{}\n\n\subsection{}\n\n\subsection{}')
    f.close()