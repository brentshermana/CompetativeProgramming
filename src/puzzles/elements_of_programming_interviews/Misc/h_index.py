# a researcher's h-index is the largest number h s.t.
# the researcher has h papers with at least h citations

def h_index(papers):
    """
    :param papers: a list of integers representing the citation count for the paper
    :return: the h-index
    """
    # papers are in order of high->low so when we're looking at a paper everything to the left has more citations
    papers.sort(reverse=True)
    h_max = 0
    for i, citations in enumerate(papers):
        if citations >= i+1:
            # both the number of papers and the number of citations are limiting factors, so
            # h is whichever is lower
            h = min(i+1, citations)
            h_max = max(h_max, h)
    return h

papers = list(range(11))
assert h_index(papers) == 5
