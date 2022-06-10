Title: Bidirectional Typing for the Calculus of Inductive Constructions
Slug: phd
Category: PhD Thesis
Lang: en
Date: 2022-06-24
Pdf_loc: 22-phd.pdf

Over their more than 50 years of existence, proof assistants have established themselves as
tools guaranteeing high trust levels in many applications.
Yet, due to their increasing complexity, the historical solution of relying on a
small, trusted kernel is not enough anymore to avoid critical bugs while moving forward.
But proof assistants have been used for decades to certify program correctness,
so why not *their own*?
This is the ambition of the MetaCoq project,
which aims at providing the first realistic kernel for a proof assistant – Coq –
to be formally proven correct, in Coq itself.
Don't trust the program anymore, only its proof!
  
This thesis studies the bidirectional structure on which the typing algorithm
implemented by the kernel of Coq relies, in the context of the Calculus of
Inductive Constructions on which it is founded. This is formalized as a part of
MetaCoq, and is a key step to reach the project’s goal,
by giving an intermediate layer between the implementation and its specification.
Moreover, the increased control over computation offered by bidirectional typing
is a necessary piece in designing a gradual extension of CIC, which aims at
bringing to development in Coq the flexibility of dynamic typing,
and forms the last part of the thesis.

