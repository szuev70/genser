# genser

The GenSer package (i.e. Generalised Serialisation) contains the set of functions to perform the dimension transformation of the numerical dataset. To use the package you should have a dataset of non-negative integer values. Having n features in your dataset, you may transform it to m features and, after your work with data, return back to n features. The following functions available:

dim_step_down(data, powers): # data is a list of lists; powers is dictionary in form {n1:N1,n2:N2}, where n1, n2 are the indices of the features being unified and N1,N2 are the corresponding powers of the features.

dim_step_up(data, powers): # data is a list of lists; powers is dictionary in form {n1:N,n2:N2}, where n1, n2 are the indices of the features: n1 will be divided onto n1 and n2, and N,N2 are the corresponding powers of the features. The resulted data will have feature n1 of power N/N2 rounded above and n2 of power N2.  

transform_to(data, m): # transforms data to the new dataset of dimension m; every step will be made with most appropriate features and the information about the step will be returned in dictionary with indexes as keys and powers as values

transform_out_down(data, story): # inverse function: performs backward transformation after dimensions growth by transform_to function; story is the dictionary given by transform_to

transform_out_up(data, story): # inverse function: performs backward transformation after dimensions decrease by transform_to function; story is the dictionary given by transform_to 
