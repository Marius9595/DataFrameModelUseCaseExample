from __future__ import annotations
import datetime
import requests as requests


def get_data_from_ree(date: datetime) -> str | Exception:
    response = requests.get(
        url='https://demanda.ree.es/WSvisionaMovilesPeninsulaRest/resources/demandaGeneracionPeninsula',
        params={
            'callback': '',
            'curva': 'DEMANDAQH',
            'fecha': date.strftime("%Y-%m-%d")
        }
    )
    if response.status_code == 200:
        content = response.text
        if content == 'formato de fecha invalido':
            raise Exception('formato de fecha invalido')
        elif content == 'curva invalida':
            raise Exception('curva invalida')
        return content
    else:
        raise Exception(response.content)