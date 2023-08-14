import pandas as pd

# finding the minimum coverage and summing the number of sites affected
def summarize_gene_data(lc_filtered):
	if 'Gene' in lc_filtered.columns:

		if 'Minimum.Depth' in lc_filtered.columns:
			if (lc_filtered['Minimum.Depth'] % 1 == 0).all():
				min_lc = lc_filtered.groupby("Gene", as_index=False)["Minimum.Depth"].min()
			else:
				raise TypeError(f"Minimum.Depth column contains non-integer whole values") # assuming that coverage cannot be a decimal value as well
		else:
			raise RuntimeError(f"'Minimum.Depth' column not found, please check the .csv file")

		if 'Number.of.Sites' in lc_filtered.columns:
			if (lc_filtered['Number.of.Sites'] % 1 == 0).all():
				sum_pos = lc_filtered.groupby("Gene", as_index=False)["Number.of.Sites"].sum()
			else:
				raise TypeError(f"Number.of.Sites column contains non-integer whole values") # assuming that number of sites cannot be a decimal value as well
		else:
			raise RuntimeError(f"'Number.of.Sites' column not found, please check the .csv file")

		gene_summary = min_lc.merge(sum_pos, on = "Gene")
		gene_summary = gene_summary.rename(columns = {"Minimum.Depth":"Minimum.Coverage", "Number.of.Sites":"Total.Low.Coverage"})
	else:
		raise RuntimeError(f"'Gene' column not found, please check the .csv file")
		
	return gene_summary