import csv
import os

from histdata.api import download_hist_data


def mkdir_p(path):
    import errno
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def download_all():
    # with open('pairs.csv', 'r') as f:
        # reader = csv.reader(f, delimiter=',')
        # next(reader, None)  # skip the headers
        # for row in reader:
            currency_pair_name='EUR/USD'
            pair = 'eurusd'
            year = int(2000)
            print(currency_pair_name)
            output_folder = os.path.join('output', pair)
            mkdir_p(output_folder)
            try:
                while True:
                    could_download_full_year = False
                    try:
                        print('-', download_hist_data(year=year,
                                                      pair=pair,
                                                      output_directory=output_folder,
                                                      verbose=False))
                        could_download_full_year = True
                    except AssertionError:
                        pass  # lets download it month by month.
                    month = 1
                    while not could_download_full_year and month <= 12:
                        print('-', download_hist_data(year=str(year),
                                                      month=str(month),
                                                      pair=pair,
                                                      output_directory=output_folder,
                                                      verbose=False))
                        month += 1
                    year += 1
            except Exception:
                print('[DONE] for currency', currency_pair_name)


if __name__ == '__main__':
    download_all()
