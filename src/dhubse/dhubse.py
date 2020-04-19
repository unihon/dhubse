import requests
from math import ceil
from tabulate import tabulate
from dhubse.utils.tool_box import color_str, localize_time, req_decorator, timing_decorator
from dhubse.utils.docker_registry_api import DOCKER_IO_API, DOCKER_HUB_API
from dhubse.utils.cli_args import set_args


class ReqHub():
    def __init__(self, timeout=5):
        self.timeout = timeout

    def _get_search_head(self):
        print_str = (
            'QUERY: '+color_str('{query:<5}')+''
            ' ITEM_COUNT: {count:<5}'
            ' PAGE_COUNT: {page_count:<5}'
            ' PAGE_SIZE: {page_size:<5}'
            ' PAGE: {page:<5}'
        )
        return '\n' + print_str + '\n'

    def _get_tag_head(self):
        print_str = (
            'IMAGE: '+color_str('{image:<5}')+''
            ' ITEM_COUNT: {count:<5}'
            ' PAGE_COUNT: {page_count:<5}'
            ' PAGE_SIZE: {page_size:<5}'
            ' PAGE: {page:<5}'
        )
        return '\n' + print_str + '\n'

    def _get_search_title(self):
        print_str = (
            '{image:<10}'
            ' {desc:<10}'
            ' {is_official:<10}'
            ' {star:<10}'
        )
        return print_str

    @req_decorator
    def _req_image_search(self, image='', page_size=20, page=1):
        url = DOCKER_IO_API.format(image=image, page_size=page_size, page=page)
        res = requests.get(url, timeout=self.timeout)
        return res

    def image_search(self, image='', page_size=20, page=1, **kwargs):
        '''search image'''

        res_dict, _ = self._req_image_search(
            image=image, page_size=page_size, page=page)

        head_str = self._get_search_head().format(
            query=image,
            count=res_dict['num_results'],
            page_count=res_dict['num_pages'] if res_dict['num_results'] else 0,
            page_size=page_size,
            page=page
        )
        info_title = self._get_search_title().format(
            image='IMAGE',
            desc='DESC',
            is_official='IS_OFFICIAL',
            star='STAR',
        )

        item_list = []
        for _item in res_dict['results']:
            f_item = [
                _item['name'],
                _item['description'][:20]+'...'
                if _item['description'] else '',
                color_str(str(_item['is_official']), color='cyan')
                if _item['is_official'] else str(_item['is_official']),
                _item['star_count'],
            ]
            item_list.append(f_item)
        table = tabulate(item_list, headers=[
                         'IMAGE', 'DESC', 'IS_OFFICIAL', 'STAR'])

        print(head_str)
        print(table)

    @req_decorator
    def _req_image_tag(self, image='', page_size=20, page=1):
        lib_image = image if '/' in image else 'library/'+image
        image = lib_image.split(':')[0]
        name = lib_image.split(':')[1] if len(lib_image.split(':')) > 1 else ''

        url = DOCKER_HUB_API.format(
            image=image, name=name, page_size=page_size, page=page)
        res = requests.get(url, timeout=self.timeout)
        return res

    def image_tag(self, image='', page_size=20, page=1, **kwargs):
        '''get image tags'''

        res_dict, _ = self._req_image_tag(
            image=image, page_size=page_size, page=page)

        head_str = self._get_tag_head().format(
            image=image,
            count=res_dict['count'],
            page_count=ceil(res_dict['count']/page_size),
            page_size=page_size,
            page=page
        )

        item_list = []
        for _item in res_dict['results']:
            f_item = [
                image.split(':')[0]+':'+_item['name'],
                _item['name'],
                '{:.2f}MB'.format(_item['full_size']/10**6),
                localize_time(_item['last_updated']),
            ]
            item_list.append(f_item)
        table = tabulate(item_list, headers=[
                         'IMAGE_NAME', 'TAG', 'FULL_SIZE', 'UPDATE'])

        print(head_str)
        print(table)


@timing_decorator
def main():
    args_dict, _ = set_args()
    mode = args_dict.pop('mode')
    timeout = args_dict.pop('timeout')
    req_hub = ReqHub(timeout=timeout)

    getattr(req_hub, 'image_'+mode)(**args_dict)


if __name__ == '__main__':
    main()
